# CNTT Cơ Bản — Project Context

## What This Project Is

A self-study workspace for Vietnamese IT/Office certification content.
YouTube lecture playlists are converted into structured Obsidian notes for offline reading and review.
Notes are written as concise **exam cheat-sheets** — key steps, tables of values, and shortcuts only.
Q&A banks are extracted from visual MCQ videos (no subtitles) using frame extraction.

## Folder Structure

```
CNTT co ban/
  .claude/
    CLAUDE.md                  ← you are here
    commands/                  ← custom slash commands
      yt-to-note.md            ← /yt-to-note
      yt-playlist.md           ← /yt-playlist
      exam-notes.md            ← /exam-notes
      video-to-qa.md           ← /video-to-qa
    scripts/                   ← Python pipeline scripts
      parse_vtt.py             ← parse raw VTT → clean text
      build_notes.py           ← one raw note per video
      merge_notes.py           ← merge into 4 part notes (legacy)
      write_exam_notes.py      ← overwrite notes with exam cheat-sheets
    rules/
      obsidian-note-format.md  ← note structure & formatting spec
  Notes/
    <Lecture name>/            ← one folder per course/playlist
      <Lecture>.md             ← index note (mục lục + checklist)
      1 - <Title>.md           ← exam note per video
      2 - <Title>.md
      ...
    Ngân Hàng Câu Hỏi <Topic>.md  ← Q&A bank extracted from MCQ video
  transcripts/                 ← raw .vi.vtt files (intermediate, safe to delete)
  playlist_info.txt            ← flat playlist dump (intermediate)
```

## Available Slash Commands

| Command | What it does |
|---------|-------------|
| `/yt-to-note` | Single YouTube video (with subtitles) → one Obsidian note |
| `/yt-playlist` | Full playlist → one raw note per video + index |
| `/exam-notes` | Rewrite all notes as concise exam cheat-sheets |
| `/video-to-qa` | Visual MCQ video (no subtitles) → Q&A bank note |

## Pipelines

**Lecture notes (video has subtitles):**
```
1. /yt-playlist   → download subtitles + build raw per-video notes
2. /exam-notes    → replace raw notes with exam-focused cheat-sheets
```

**Q&A bank (video has no subtitles, MCQ slides only):**
```
1. /video-to-qa   → download video → extract frames → read Q&A → write bank note
```

## Key Rules

- Notes are always in **Vietnamese**
- Subtitles: `yt-dlp --sub-lang vi --write-auto-subs`
- Auto-captions have recognition errors — always verify key values
- **One note per video** (bài), not merged parts
- Note filenames: `N - <Title>.md` (no lecture prefix, no "Bài")
- Each exam note = steps + value tables + shortcuts + ⚠️ common mistakes
- Obsidian wikilinks: `[[Lecture name]]` for index, `[[N - Title]]` between notes
- Q&A bank: grouped by topic, answer in `> **Đáp án: ...**` blockquote
- Full format spec: `.claude/rules/obsidian-note-format.md`

## Dependencies

```
python     # 3.x, available as `python`
yt-dlp     # pip install yt-dlp
ffmpeg     # winget install "Gyan.FFmpeg"  ← required for /video-to-qa
```

**yt-dlp YouTube workarounds:**
- No JS runtime: use `--extractor-args "youtube:player_client=android,web"`
- Bot detection (HTTP 429): add `--cookies-from-browser chrome` (close Chrome first)
- Chrome DPAPI cookie error: try Edge, or export cookies manually via browser extension
