# CNTT Cơ Bản — Self-Study Workspace

Obsidian notes for Vietnamese IT/Office certification (CNTT) exam prep.
YouTube lecture playlists → structured cheat-sheet notes + MCQ Q&A banks.

---

## Requirements

| Tool | Install | Check |
|------|---------|-------|
| Python 3.x | [python.org](https://www.python.org) | `python --version` |
| yt-dlp | `pip install yt-dlp` | `python -m yt_dlp --version` |
| ffmpeg | `winget install "Gyan.FFmpeg" --accept-package-agreements --accept-source-agreements` | `ffmpeg -version` |
| Obsidian | [obsidian.md](https://obsidian.md) | Open `Notes/` as vault |

> **After installing ffmpeg via winget**, open a new terminal — or manually refresh PATH in the current session:
> ```powershell
> $env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
> ```

---

## Folder Structure

```
CNTT co ban/
  README.md                  ← this file
  .claude/
    CLAUDE.md                ← project rules for Claude Code
    commands/                ← slash commands (/yt-playlist, /video-to-qa, ...)
    scripts/                 ← Python pipeline scripts
    rules/                   ← note format spec
  Notes/
    Word lecture/            ← one folder per course
      Word lecture.md        ← index note (mục lục + checklist)
      1 - Title.md           ← exam cheat-sheet per video
      2 - Title.md
      ...
    Ngân Hàng Câu Hỏi Trắc Nghiệm CNTT.md   ← MCQ bank
  transcripts/               ← intermediate .vtt files (safe to delete)
  playlist_info.txt          ← intermediate playlist dump (safe to delete)
```

---

## Pipelines

### Pipeline A — Lecture Notes (video has subtitles)

```
YouTube playlist
    ↓  /yt-playlist
Raw per-video notes (transcripts)
    ↓  /exam-notes
Exam cheat-sheets (final)
```

**Step 1 — Download playlist subtitles and build raw notes**

```powershell
$env:PYTHONIOENCODING = "utf-8"
# List all videos
python -m yt_dlp --extractor-args "youtube:player_client=android,web" `
  --flat-playlist --print "%(playlist_index)s|%(id)s|%(title)s" "<playlist URL>" `
  2>&1 | Where-Object { $_ -match "^\d+\|" } `
  | Out-File -Encoding utf8 "d:\Dev n Code\CNTT co ban\playlist_info.txt"

# Download Vietnamese subtitles for each video
$outDir = "d:\Dev n Code\CNTT co ban\transcripts"
python -m yt_dlp --extractor-args "youtube:player_client=android,web" `
  --write-auto-subs --sub-lang "vi" --skip-download `
  --output "$outDir\%(playlist_index)s_%(title)s" "<playlist URL>"
```

**Step 2 — Run exam-notes script**

Edit `NOTES_DIR`, `LECTURE`, and `NOTES` dict in `.claude/scripts/write_exam_notes.py`, then:

```powershell
$env:PYTHONIOENCODING = "utf-8"
python ".claude\scripts\write_exam_notes.py"
```

---

### Pipeline B — MCQ Q&A Bank (video has no subtitles, visual slides)

```
YouTube MCQ video
    ↓  /video-to-qa
Frame extraction (ffmpeg)
    ↓
Read frames in batches
    ↓
Notes/Ngân Hàng Câu Hỏi <Topic>.md
```

**Step 1 — Download video**

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
$env:PYTHONIOENCODING = "utf-8"
New-Item -ItemType Directory -Force "d:\Dev n Code\CNTT co ban\frames"
python -m yt_dlp --extractor-args "youtube:player_client=android,web" `
  -f "bestvideo[ext=mp4]/best[ext=mp4]/best" `
  -o "d:\Dev n Code\CNTT co ban\frames\video.%(ext)s" `
  "<url>"
```

**Step 2 — Extract frames**

```powershell
ffmpeg -i "d:\Dev n Code\CNTT co ban\frames\video.mp4" `
  -vf "fps=1/3,scale=1280:-1" -q:v 2 `
  "d:\Dev n Code\CNTT co ban\frames\frame_%04d.jpg"
```

**Step 3 — Read frames and write note**

Read frames in batches of 5. For each unique question, record question text, 4 options, and correct answer. Write to `Notes/Ngân Hàng Câu Hỏi <Topic>.md`.

**Step 4 — Clean up**

```powershell
Remove-Item -Recurse -Force "d:\Dev n Code\CNTT co ban\frames" -Confirm:$false
```

---

## Slash Commands (Claude Code)

| Command | Usage |
|---------|-------|
| `/yt-playlist` | Full playlist → per-video raw notes + index |
| `/exam-notes` | Rewrite raw notes as exam cheat-sheets |
| `/yt-to-note` | Single video → one note |
| `/video-to-qa` | Visual MCQ video → Q&A bank note |

Command specs are in `.claude/commands/`.

---

## Known Errors & Fixes (Windows)

### 1. yt-dlp: Chrome DPAPI decryption error

```
ERROR: Failed to decrypt with DPAPI
```

**Cause:** Chrome v127+ changed cookie encryption; yt-dlp cannot decrypt cookies.
**Fix:** Use the android player client — no cookies needed:

```powershell
python -m yt_dlp --extractor-args "youtube:player_client=android,web" ...
```

### 2. yt-dlp: Edge/Chrome cookie database locked

```
ERROR: Could not copy Chrome cookie database
```

**Cause:** The browser is open and holds a lock on its SQLite cookie file.
**Fix:** Close the browser first, or use the android client workaround above.

### 3. yt-dlp: HTTP 429 Too Many Requests

```
WARNING: [youtube] HTTP Error 429 ...
```

**Cause:** YouTube rate-limiting the request.
**Behaviour:** Non-fatal when using `--extractor-args "youtube:player_client=android,web"` — the android player API endpoint still responds.
**Fix:** Usually resolves itself; if persistent, add `--sleep-requests 2`.

### 4. ffmpeg not found after winget install

```
ffmpeg : The term 'ffmpeg' is not recognized
```

**Cause:** winget installs to a PATH entry that the current PowerShell session doesn't see yet.
**Fix:** Refresh PATH without opening a new terminal:

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
```

### 5. PowerShell 5.1 — null-conditional `?.` operator not supported

```
ParserError: Unexpected token '?.'
```

**Cause:** Windows ships with PowerShell 5.1 which doesn't support `?.`, `??`, or `&&`/`||` pipeline chain operators.
**Fix:** Use explicit checks:

```powershell
# Instead of: $obj?.Property
if ($obj -ne $null) { $obj.Property }

# Instead of: A && B
A; if ($?) { B }
```

---

## Notes Format

See `.claude/rules/obsidian-note-format.md` for the full spec.
Key points:
- Exam notes: steps + value tables + shortcuts + one `⚠️` warning, under 80 lines
- Q&A banks: grouped by topic, answer in `> **Đáp án: ...**` blockquote
- Note filenames: `N - Title.md` (no lecture prefix, no "Bài")
- Navigation links: `← [[N-1 - PrevTitle|Bài N-1]]  |  [[Lecture|📋 Mục lục]]  |  [[N+1 - NextTitle|Bài N+1]] →`
