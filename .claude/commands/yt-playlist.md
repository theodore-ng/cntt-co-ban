Convert a full YouTube playlist into structured Obsidian exam notes (index + one note per video).

## Usage

```
/yt-playlist <playlist URL> <lecture name>
```

- `<playlist URL>` — full YouTube playlist URL
- `<lecture name>` — folder and index note name, e.g. `Word lecture`, `Excel lecture`

## Full Pipeline

```
YouTube playlist
    ↓  Step 1 — fetch video list
    ↓  Step 2 — download Vietnamese subtitles (VTT)
    ↓  Step 3 — parse VTTs → read transcript content
    ↓  Step 4 — write lecture-specific exam script
    ↓  Step 5 — run script → generate N exam notes
    ↓  Step 6 — write index note
    ↓  Step 7 — git commit & push
Notes/<lecture name>/<N> - <Title>.md  ✓
```

---

## Steps to Execute

### Step 1 — Fetch video list

```powershell
$env:PYTHONIOENCODING = "utf-8"
python -m yt_dlp --extractor-args "youtube:player_client=android,web" `
  --flat-playlist --print "%(playlist_index)s|%(id)s|%(title)s" `
  "<playlist URL>" 2>&1 `
  | Where-Object { $_ -match "^\d+\|" } `
  | Out-File -Encoding utf8 "d:\Dev n Code\CNTT co ban\playlist_info.txt"
Get-Content "d:\Dev n Code\CNTT co ban\playlist_info.txt" -Encoding utf8
```

Note video IDs and titles in **lesson order** (Bài 1 first). Playlists are often uploaded in reverse — match Bài number from the title text, not playlist index.
Skip any video where title is `NA` (private/unavailable).

---

### Step 2 — Download Vietnamese subtitles

```powershell
$env:PYTHONIOENCODING = "utf-8"
$outDir = "d:\Dev n Code\CNTT co ban\transcripts"
python -m yt_dlp --extractor-args "youtube:player_client=android,web" `
  --write-auto-subs --sub-lang "vi" --skip-download `
  --output "$outDir\%(playlist_index)s_%(title)s" `
  "<playlist URL>"
```

Confirm each `*.vi.vtt` exists in `transcripts/`. NA videos will error — ignore.

---

### Step 3 — Parse VTTs and read content

Parse each VTT in playlist-index order:

```powershell
$env:PYTHONIOENCODING = "utf-8"
$transcripts = "d:\Dev n Code\CNTT co ban\transcripts"
for ($i = 1; $i -le <N>; $i++) {
    $file = Get-ChildItem $transcripts -Filter "${i}_*.vi.vtt" | Select-Object -First 1
    if ($file) {
        Write-Host "=== $($file.Name) ===" -ForegroundColor Cyan
        python ".claude\scripts\parse_vtt.py" $file.FullName
        Write-Host ""
    }
}
```

Read all transcript output. For each Bài identify:
- Main topic and key steps (menu paths)
- Important values (numbers, settings, shortcuts)
- Common mistakes mentioned by the instructor

---

### Step 4 — Write the exam notes script

Create `.claude/scripts/write_<slug>_exam_notes.py` modelled on an existing one (e.g. `write_excel_exam_notes.py`).

Fill in `NOTES_DIR`, `LECTURE`, and the `NOTES` dict:

```python
NOTES_DIR = r"d:\Dev n Code\CNTT co ban\Notes\<lecture name>"
LECTURE   = "<lecture name>"

NOTES = {
    1: ("Title", """### Section\n\n`Menu → Path → Command`\n\n| Key | Value |\n..."""),
    2: ("Title", """..."""),
}
```

Content rules per lesson (keep under ~30 lines each):
- Steps in `` `Menu → Path → Command` `` backtick format
- Tables for memorizable values — **bold** the most important
- `> **Nhớ nhanh: ...**` for rules of thumb
- One `⚠️` per lesson — the single most-tested gotcha
- Keyboard shortcuts in `| Phím | Chức năng |` table
- No prose, no transcript text

Tags: course slug (`word`, `excel`, `powerpoint`) + `cntt-co-ban` + `exam-note`.

---

### Step 5 — Run the script

```powershell
$env:PYTHONIOENCODING = "utf-8"
python ".claude\scripts\write_<slug>_exam_notes.py"
```

---

### Step 6 — Write the index note

Create `Notes/<lecture name>/<lecture name>.md`:

```markdown
# <Lecture Name> — <Course subtitle>

> 📺 [YouTube Playlist](<url>)
> 🗂️ N bài

---

## Mục Lục

| Bài | Chủ đề |
|-----|--------|
| [[1 - Title\|Bài 1]] | Title |
...

---

## Checklist Học Tập

- [ ] Bài 1 — Title
...

---

> [!tip] Mẹo học hiệu quả
> Đọc note → Thực hành trong <App> → Tick checklist
```

---

### Step 7 — Verify, commit, push

```powershell
# Verify
Get-ChildItem "d:\Dev n Code\CNTT co ban\Notes\<lecture name>" -Filter *.md | Select-Object Name

# Commit and push
git add "Notes/<lecture name>/" ".claude/scripts/write_<slug>_exam_notes.py"
git commit -m "Add <lecture name> notes (N bài)"
git push
```

Expected structure:
```
Notes/<lecture name>/
  <lecture name>.md       ← index note
  1 - <Title>.md
  2 - <Title>.md
  ...
  N - <Title>.md
```

---

## Known Errors (Windows)

### yt-dlp: Chrome DPAPI / cookie errors
```
ERROR: Failed to decrypt with DPAPI
ERROR: Could not copy Chrome cookie database
```
**Fix:** `--extractor-args "youtube:player_client=android,web"` in all commands above bypasses this — no browser needed.

### yt-dlp: HTTP 429 Too Many Requests
Non-fatal with the android client. If persistent, add `--sleep-requests 2`.

### NA videos
Videos with `NA` title are private/deleted. Subtitle download will error — ignore and continue.

---

## Note Format

Follow `.claude/rules/obsidian-note-format.md` exactly.
Navigation: `← [[N-1 - PrevTitle|Bài N-1]]  |  [[Lecture|📋 Mục lục]]  |  [[N+1 - NextTitle|Bài N+1]] →`
