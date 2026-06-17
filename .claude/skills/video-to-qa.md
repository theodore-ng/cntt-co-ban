Extract multiple-choice Q&A from a YouTube video that has no subtitles (visual slide-based content) by downloading and reading video frames.

## Usage

```
/video-to-qa <url> [topic name]
```

- `<url>` — YouTube video URL
- `[topic name]` — optional label for the output note (e.g. "CNTT Cơ Bản", "Excel")

## When to use

Use this instead of `/yt-to-note` when:
- The video has **no subtitles** (`yt-dlp --list-subs` returns nothing)
- Content is purely visual: MCQ slides, images of questions scrolling on screen
- Auto-captions are absent because there is no speech

## Prerequisites

**ffmpeg** must be installed. If missing:
```powershell
winget install "Gyan.FFmpeg" --accept-package-agreements --accept-source-agreements
```
Then open a new terminal (PATH refresh needed).

**yt-dlp** must be available:
```powershell
pip install yt-dlp
```

## Steps to Execute

### Step 1 — Check for subtitles first

```powershell
$env:PYTHONIOENCODING = "utf-8"
python -m yt_dlp --list-subs "<url>"
```

If result shows `has no automatic captions` → proceed with frame extraction.
If subtitles exist → use `/yt-to-note` instead.

### Step 2 — Create frames folder

```powershell
New-Item -ItemType Directory -Force "d:\Dev n Code\CNTT co ban\frames"
```

### Step 3 — Download video

YouTube requires the Android client workaround (no JS runtime needed):

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
$env:PYTHONIOENCODING = "utf-8"
python -m yt_dlp --extractor-args "youtube:player_client=android,web" `
  -f "bestvideo[ext=mp4]/best[ext=mp4]/best" `
  -o "d:\Dev n Code\CNTT co ban\frames\video.%(ext)s" `
  "<url>"
```

If you get HTTP 429 or bot-detection errors, add `--cookies-from-browser chrome` (requires Chrome to be **closed** first).

### Step 4 — Extract frames

One frame every 3 seconds is enough for slide-based videos:

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
ffmpeg -i "d:\Dev n Code\CNTT co ban\frames\video.mp4" `
  -vf "fps=1/3,scale=1280:-1" -q:v 2 `
  "d:\Dev n Code\CNTT co ban\frames\frame_%04d.jpg"
```

Check frame count:
```powershell
(Get-ChildItem "d:\Dev n Code\CNTT co ban\frames" -Filter "frame_*.jpg").Count
```

### Step 5 — Read frames and extract Q&A

Read frames in parallel batches of 5, skipping duplicates (the video often holds on a slide for multiple seconds). For each unique question found, record:

- Question text
- All 4 options (a, b, c, d)
- Correct answer (marked with ✓ on screen, or shown in yellow "Đáp án đúng là:" line)

### Step 6 — Write the Obsidian note

Append to `Notes/QA Bank.md` (create if first run). Group questions by topic (Word, Excel, PowerPoint, Internet, Windows, Bảo mật, Kiến thức chung). See output format below.

### Step 7 — Clean up

```powershell
Remove-Item -Recurse -Force "d:\Dev n Code\CNTT co ban\frames"
```

## Output note format

```markdown
---
title: "QA Bank"
tags:
  - cntt-co-ban
  - trac-nghiem
  - on-thi
source: "<url>"
---

# QA Bank

> 🗂️ N câu · K chủ đề

---

## 1. <Chủ đề>

**Câu N.** <Câu hỏi>?

- a. ...
- b. ...
- c. ...
- d. ...

> **Đáp án: <x>. <Nội dung đúng>**

---

## Ghi Chú Cá Nhân

> [!question] Chưa hiểu
> -

> [!check] Đã nắm
> -

> [!tip] Mẹo ôn tập
> Đọc câu hỏi → Tự chọn đáp án → Mở "Đáp án" để kiểm tra
```

## Notes

- Each screen typically shows 2–3 questions; frames at 3-second intervals capture each one
- The yellow "Đáp án đúng là:" line confirms the correct answer — always use this, not the ✓ highlight alone
- Some slides may repeat across frames — deduplicate by question text before writing
- If a question is partially cut off at the bottom of a frame, read the next frame to get the full text
- Some videos show no answer highlights at all — cross-reference with an existing Q&A bank and use CNTT knowledge for answers

## Known Errors (Windows)

### ffmpeg not found after winget install

```
ffmpeg : The term 'ffmpeg' is not recognized as the name of a cmdlet...
```

**Cause:** winget adds ffmpeg to PATH but the current PowerShell session doesn't pick it up.
**Fix:** Refresh PATH in the current session (no need to open a new terminal):

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
```

### yt-dlp: Chrome DPAPI decryption error

```
ERROR: Failed to decrypt with DPAPI
```

**Cause:** Chrome v127+ changed cookie encryption; yt-dlp cannot read cookies.
**Fix:** The android client in Step 3 (`--extractor-args "youtube:player_client=android,web"`) bypasses this entirely — no cookies needed.

### yt-dlp: Edge cookie database locked

```
ERROR: Could not copy Chrome cookie database
```

**Cause:** Edge is open and holds a lock on its SQLite cookie file.
**Fix:** Same android client workaround — never requires a browser to be open or closed.

### yt-dlp: HTTP 429 Too Many Requests

Non-fatal when using the android client. YouTube may still rate-limit metadata requests but the video download proceeds via the android player API. If the download stalls, add `--sleep-requests 2`.
