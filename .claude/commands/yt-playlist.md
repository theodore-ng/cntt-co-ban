Convert a full YouTube playlist into structured Obsidian exam notes (index + one note per video).

## Usage

```
/yt-playlist <playlist URL> <lecture name>
```

- `<playlist URL>` — full YouTube playlist URL
- `<lecture name>` — folder and note prefix, e.g. `Word lecture`, `Excel lecture`

## Steps to Execute

### Step 1 — Check dependencies
```powershell
python --version
python -m yt_dlp --version
# If missing: pip install yt-dlp
```

### Step 2 — Get all video IDs and titles
```powershell
$env:PYTHONIOENCODING = "utf-8"
python -m yt_dlp --extractor-args "youtube:player_client=android,web" `
  --flat-playlist --print "%(playlist_index)s|%(id)s|%(title)s" "<playlist URL>" 2>&1 `
  | Where-Object { $_ -match "^\d+\|" } `
  | Out-File -Encoding utf8 "d:\Dev n Code\CNTT co ban\playlist_info.txt"
Get-Content "d:\Dev n Code\CNTT co ban\playlist_info.txt" -Encoding utf8
```

Skip any video with `NA` in the title (private/unavailable).

### Step 3 — Download Vietnamese subtitles for all videos
```powershell
$outDir = "d:\Dev n Code\CNTT co ban\transcripts"
python -m yt_dlp --extractor-args "youtube:player_client=android,web" `
  --write-auto-subs --sub-lang "vi" --skip-download `
  --output "$outDir\%(playlist_index)s_%(title)s" `
  "<playlist URL>"
```

### Step 4 — Parse VTTs and build per-video notes
Run `.claude/scripts/build_notes.py` after updating its `VIDEO_MAP`, `TRANSCRIPTS_DIR`, and `NOTES_DIR` constants to match the current playlist.

```powershell
$env:PYTHONIOENCODING = "utf-8"
python ".claude\scripts\build_notes.py"
```

This produces one `.md` per video in `Notes\<lecture name>\`.

### Step 5 — Rewrite notes as exam cheat-sheets

Run `/exam-notes <lecture name>` — see `.claude/commands/exam-notes.md`.

### Step 6 — Verify structure
```powershell
Get-ChildItem "d:\Dev n Code\CNTT co ban\Notes\<lecture name>" -Filter *.md | Select-Object Name
```

Expected output:
```
<Lecture name>.md     ← index note
1 - Title.md
2 - Title.md
...
N - Title.md
```

## Known Errors (Windows)

### yt-dlp: Chrome DPAPI / cookie errors
```
ERROR: Failed to decrypt with DPAPI
ERROR: Could not copy Chrome cookie database
```
**Fix:** Use the android player client instead of cookies — no browser needed:
```powershell
--extractor-args "youtube:player_client=android,web"
```
This is already included in all commands above.

### yt-dlp: HTTP 429 Too Many Requests
Non-fatal when using the android client. The android player API endpoint still responds. If persistent, add `--sleep-requests 2`.

### Subtitles unavailable (NA videos)
Videos with `NA` in `playlist_info.txt` are private or deleted. Skip them — do not include their IDs in Step 3.

## Note Format

Follow `.claude/rules/obsidian-note-format.md` exactly.
