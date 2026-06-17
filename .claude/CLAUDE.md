# CNTT Cơ Bản — Project Context

## What This Project Is

A self-study workspace for Vietnamese IT/Office certification content.
YouTube lecture playlists are converted into structured Obsidian notes for offline reading and review.
Notes are written as concise **exam cheat-sheets** — key steps, tables of values, and shortcuts only.
Q&A banks are extracted from visual MCQ videos (no subtitles) using frame extraction.

## Folder Structure

```
CNTT co ban/
  README.md                    ← Windows pipeline guide + known errors
  .claude/
    CLAUDE.md                  ← you are here
    commands/                  ← slash command skill specs
      yt-playlist.md           ← /yt-playlist  (full pipeline)
      exam-notes.md            ← /exam-notes   (rewrite as cheat-sheets)
      yt-to-note.md            ← /yt-to-note   (single video)
      video-to-qa.md           ← /video-to-qa  (MCQ bank)
    scripts/                   ← Python pipeline scripts
      parse_vtt.py             ← parse raw VTT → clean text
      build_notes.py           ← (legacy) raw transcript notes
      write_exam_notes.py      ← Word lecture exam notes
      write_ppt_exam_notes.py  ← PowerPoint lecture exam notes
      write_excel_exam_notes.py← Excel lecture exam notes
    rules/
      obsidian-note-format.md  ← note structure & formatting spec
  Notes/
    Word lecture/              ← 15 exam notes + index
    PowerPoint lecture/        ← 5 exam notes + index
    Excel lecture/             ← 8 exam notes + index
    Ngân Hàng Câu Hỏi Trắc Nghiệm CNTT.md  ← 53-question MCQ bank
  transcripts/                 ← raw .vi.vtt files (intermediate, safe to delete)
  playlist_info.txt            ← flat playlist dump (intermediate)
```

## Available Skills

| Skill | Command | What it does |
|-------|---------|-------------|
| `yt-playlist` | `/yt-playlist <url> <name>` | Full playlist → exam notes (complete pipeline) |
| `exam-notes` | `/exam-notes <name>` | Write/update lecture-specific exam script |
| `yt-to-note` | `/yt-to-note <url>` | Single video → one note |
| `video-to-qa` | `/video-to-qa <url>` | Visual MCQ video → Q&A bank |

## Lecture Pipeline (video has subtitles)

```
1. /yt-playlist  →  fetch playlist info + download VTT subtitles
2.               →  parse VTTs, read all transcript content
3. /exam-notes   →  create write_<slug>_exam_notes.py + run it
4.               →  write index note
5.               →  git commit & push
```

Each lecture gets its own dedicated exam script in `.claude/scripts/`:

| Lecture | Script |
|---------|--------|
| Word lecture (15 bài) | `write_exam_notes.py` |
| PowerPoint lecture (5 bài) | `write_ppt_exam_notes.py` |
| Excel lecture (8 bài) | `write_excel_exam_notes.py` |
| New lectures | `write_<slug>_exam_notes.py` |

## Q&A Bank Pipeline (video has no subtitles, MCQ slides)

```
1. /video-to-qa  →  download video → extract frames (ffmpeg) → read Q&A → write bank note
```

## Key Rules

- Notes always in **Vietnamese**
- Subtitles: `yt-dlp --sub-lang vi --write-auto-subs`
- Auto-captions have recognition errors — verify key values against domain knowledge
- **One note per video** (bài), not merged parts
- Note filenames: `N - <Title>.md` (no lecture prefix, no "Bài")
- Each exam note = steps + value tables + shortcuts + ⚠️ common mistake
- Obsidian wikilinks: `[[Lecture name]]` for index, `[[N - Title|Bài N]]` between notes
- Q&A bank: grouped by topic, answer in `> **Đáp án: ...**` blockquote
- Full format spec: `.claude/rules/obsidian-note-format.md`

## Dependencies

```
python     # 3.x, available as `python`
yt-dlp     # pip install yt-dlp
ffmpeg     # winget install "Gyan.FFmpeg"  ← required for /video-to-qa
gh         # winget install GitHub.cli     ← for git push / repo management
```

**yt-dlp YouTube workarounds (Windows):**
- Always use: `--extractor-args "youtube:player_client=android,web"`
- This bypasses: Chrome DPAPI cookie errors, Edge lock, bot detection
- ffmpeg PATH after winget: `$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")`
