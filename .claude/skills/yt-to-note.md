Convert a single YouTube video into a structured Obsidian note.

## Usage

```
/yt-to-note <YouTube URL> [output folder name]
```

- `<YouTube URL>` — the video URL (with or without playlist params)
- `[output folder name]` — optional, defaults to the video title's course name

## Steps to Execute

1. **Check dependencies**
   ```powershell
   python --version
   python -m yt_dlp --version
   # If yt-dlp missing: pip install yt-dlp
   ```

2. **Get video title**
   ```powershell
   $env:PYTHONIOENCODING = "utf-8"
   python -m yt_dlp --get-title "<URL>" 2>&1 | Where-Object { $_ -notmatch "WARNING|Downloading|Extracting" }
   ```

3. **Download Vietnamese subtitles**
   ```powershell
   $env:PYTHONIOENCODING = "utf-8"
   $outDir = "d:\Dev n Code\CNTT co ban\transcripts"
   python -m yt_dlp --extractor-args "youtube:player_client=android,web" `
     --write-auto-subs --sub-lang "vi" --skip-download `
     --output "$outDir\%(title)s" "<URL>"
   ```
   - `--extractor-args "youtube:player_client=android,web"` bypasses Chrome DPAPI and cookie errors
   - If `vi` subtitles are unavailable, fall back to `--sub-lang en`
   - Confirm the `.vi.vtt` file exists in `transcripts/`

4. **Parse VTT to clean text**
   ```powershell
   $env:PYTHONIOENCODING = "utf-8"
   python ".claude\scripts\parse_vtt.py" "<path-to.vi.vtt>" | Out-File -Encoding utf8 "transcripts\clean.txt"
   ```

5. **Build the Obsidian note**
   - Read `transcripts\clean.txt`
   - Determine bài number and title from video title
   - Apply format from `.claude/rules/obsidian-note-format.md` (single-video variant)
   - Write to `Notes\<output folder>\<note name>.md`

6. **Verify** — confirm the note file exists and open it

## Output Format (single note)

```markdown
---
title: "<Course> - <Bài N>: <Title>"
tags: [<course>, cntt-co-ban, <slug>]
source: "<URL>"
---

# Bài N: <Title>

> [!info] Nguồn
> 📺 [YouTube – <Title>](<URL>)

---

## Nội Dung Bài Học

> *Bản ghi được tổng hợp từ phụ đề tự động...*

<transcript paragraphs>

---

## Ghi Chú Cá Nhân

> [!question] ...
> [!check] ...
> [!todo] ...
```
