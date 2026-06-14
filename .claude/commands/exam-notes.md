Rewrite all per-video notes in a lecture folder as concise exam cheat-sheets.

## Usage

```
/exam-notes <lecture name>
```

- `<lecture name>` — the lecture folder name, e.g. `Word lecture`, `Excel lecture`

## When to use

Run this **after** `/yt-playlist` has generated raw transcript notes.
It replaces the verbose transcript content with structured, exam-ready summaries.

## Steps to Execute

### Step 1 — Edit the script constants

Open `.claude/scripts/write_exam_notes.py` and update:

```python
NOTES_DIR = r"d:\Dev n Code\CNTT co ban\Notes\<lecture name>"
LECTURE   = "<lecture name>"
```

### Step 2 — Fill in the NOTES dict

The `NOTES` dict maps lesson number → (title, exam_content).
`exam_content` is a markdown string containing only:

- **Numbered steps** with `Menu → Path → Command` format
- **Tables** for values that must be memorized
- `> **Nhớ nhanh: ...**` callouts for rules of thumb
- `⚠️` prefix for the single most-tested gotcha per lesson
- **Keyboard shortcuts** in a table

Keep each lesson under ~30 lines. No prose, no transcript text.

### Step 3 — Run

```powershell
$env:PYTHONIOENCODING = "utf-8"
python ".claude\scripts\write_exam_notes.py"
```

### Step 4 — Verify

```powershell
Get-ChildItem "d:\Dev n Code\CNTT co ban\Notes\<lecture name>" -Filter *.md | Select-Object Name
```

Each `<Lecture> Bài N - <Title>.md` should exist and be under 80 lines.

## Output note structure (per bài)

```markdown
---
title: "<Lecture> - Bài N: <Title>"
tags: [word, cntt-co-ban, exam-note]
---

# Bài N: <Title>

← [[prev]] | [[index]] | [[next]] →

---

### <Section heading>

`Menu → Path → Command`

| Key value | Value |
|-----------|-------|
| ...       | ...   |

> **Nhớ nhanh: rule**

---

## Ghi Chú Cá Nhân

> [!question] Chưa hiểu
> [!check] Đã nắm
```

## Editing exam content later

To update a single lesson's content, edit the relevant entry in the `NOTES` dict
inside `write_exam_notes.py` and re-run the script. The file is overwritten cleanly.
