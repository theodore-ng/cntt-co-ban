Rewrite all per-video notes in a lecture folder as concise exam cheat-sheets.

## Usage

```
/exam-notes <lecture name>
```

- `<lecture name>` — the lecture folder name, e.g. `Word lecture`, `Excel lecture`

## When to use

Run this as **Step 4–5** of `/yt-playlist` after parsing the VTT transcripts.
Each lecture gets its own dedicated script (e.g. `write_excel_exam_notes.py`) so content can be updated independently.

---

## Steps to Execute

### Step 1 — Create the lecture exam script

Copy the closest existing script as a template:

```powershell
Copy-Item ".claude\scripts\write_excel_exam_notes.py" ".claude\scripts\write_<slug>_exam_notes.py"
```

Update the constants at the top:

```python
NOTES_DIR = r"d:\Dev n Code\CNTT co ban\Notes\<lecture name>"
LECTURE   = "<lecture name>"
```

---

### Step 2 — Fill in the NOTES dict

Each entry: `lesson_number: ("Title", "markdown_body")`

```python
NOTES = {
1: (
"Tên Bài 1",
"""### Section heading

`Menu → Path → Command`

| Cột A | Cột B |
|-------|-------|
| ...   | **giá trị quan trọng** |

> **Nhớ nhanh: quy tắc ngắn gọn**

⚠️ Lỗi phổ biến nhất trong bài này
"""),

2: (
"Tên Bài 2",
"""..."""),
}
```

**Content rules (per lesson, under ~30 lines):**
- Steps: `` `Menu → Path → Command` `` (backtick code span)
- Tables for values/shortcuts that must be memorized
- Bold (`**...**`) the single most important value per table
- `> **Nhớ nhanh: ...**` — one key rule of thumb
- `⚠️` — one line, the single most-tested exam gotcha
- No prose, no transcript text

---

### Step 3 — Run the script

```powershell
$env:PYTHONIOENCODING = "utf-8"
python ".claude\scripts\write_<slug>_exam_notes.py"
```

---

### Step 4 — Verify

```powershell
Get-ChildItem "d:\Dev n Code\CNTT co ban\Notes\<lecture name>" -Filter *.md | Select-Object Name
```

Files should be named `N - Title.md` (no lecture prefix, no "Bài").

---

## Existing lecture scripts

| Lecture | Script |
|---------|--------|
| Word lecture | `.claude/scripts/write_exam_notes.py` |
| PowerPoint lecture | `.claude/scripts/write_ppt_exam_notes.py` |
| Excel lecture | `.claude/scripts/write_excel_exam_notes.py` |

To update a single lesson: edit the entry in the script's `NOTES` dict → re-run the script. Files are overwritten cleanly.

---

## Output note structure

```markdown
---
title: "<Lecture> - Bài N: <Title>"
tags:
  - <course-slug>
  - cntt-co-ban
  - exam-note
---

# Bài N: <Title>

← [[N-1 - PrevTitle|Bài N-1]]  |  [[Lecture|📋 Mục lục]]  |  [[N+1 - NextTitle|Bài N+1]] →

---

### <Section>

`Menu → Path → Command`

| Key | Value |
|-----|-------|
| ... | **val** |

> **Nhớ nhanh: ...**

⚠️ Common mistake

---

## Ghi Chú Cá Nhân

> [!question] Chưa hiểu
> -

> [!check] Đã nắm
> -

---

← [[...]] | [[...]] | [[...]] →
```
