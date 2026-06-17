Extract Q&A from a screenshot of an online Vietnamese IT exam and append new questions to the Q&A bank. The correct answer is already marked in the image — no verification needed, just read and record what is highlighted.

## Usage

```
/screenshot-to-qa <image-path>
```

Example: `/screenshot-to-qa data/1.png`

Multiple images: run once per file, or pass a folder and process each image in order.

---

## Steps to Execute

### Step 1 — Slice the image into readable chunks

Screenshots are full-page captures (typically 1800×16000+ px). Slice vertically into 1200 px chunks:

```python
from PIL import Image
import os

img = Image.open('<image-path>')
w, h = img.size
chunk_h = 1200
os.makedirs('data/chunks', exist_ok=True)
slug = os.path.splitext(os.path.basename('<image-path>'))[0]
for i, y in enumerate(range(0, h, chunk_h)):
    crop = img.crop((0, y, w, min(y + chunk_h, h)))
    crop.save(f'data/chunks/{slug}_{i:02d}.png')
print(f"Sliced into {i+1} chunks")
```

---

### Step 2 — Read all chunks and extract Q&A

Read every `data/chunks/{slug}_NN.png` in order (batches of 4 in parallel). For each question found, record:

- Question text (full sentence)
- All 4 options (a / b / c / d) with exact wording
- **Correct answer = the option highlighted in yellow** — read it exactly as shown, do not re-evaluate

A question may span two adjacent chunks — always confirm the answer from the next chunk before recording.

---

### Step 3 — Read the current bank

Read `Notes/QA Bank.md` to get:
1. Current highest question number → next new question = highest + 1
2. All existing question texts → for duplicate check

---

### Step 4 — Deduplicate against existing bank

For each extracted question, compare its text (normalised: lowercase, strip punctuation) against all existing bank entries. **Skip** if substantially the same question already exists. If wording differs but the knowledge tested is identical and options are the same → skip.

Log all skipped questions with reason.

---

### Step 5 — Classify by topic

Map each new question to one of the 7 bank sections:

| Keywords in question | Section |
|---|---|
| Word, văn bản, soạn thảo, Style, Text Direction | 1. Microsoft Word |
| PowerPoint, slide, trình chiếu, hiệu ứng | 2. Microsoft PowerPoint |
| Excel, bảng tính, hàm, ô, SUM, VLOOKUP | 3. Microsoft Excel |
| email, internet, trình duyệt, web, attachment | 4. Email & Internet |
| Windows, hệ điều hành, thư mục, tệp, Unikey | 5. Windows & Hệ Điều Hành |
| virus, antivirus, bảo mật, mật khẩu, firewall | 6. Bảo Mật & Phần Mềm Độc Hại |
| MBps, VoIP, mạng LAN, phần mềm, tên miền, CNTT | 7. Kiến Thức Chung CNTT |

---

### Step 6 — Format each new question

```markdown
**Câu N.** <Question text>?

- a. <option>
- b. <option>
- c. <option>
- d. <option>

> **Đáp án: <letter>. <highlighted answer text>**

---
```

Number sequentially from (current highest + 1).

---

### Step 7 — Insert into bank

Use `Edit` to append new questions at the end of their topic section — just before the next `## N.` heading (or before `## Ghi Chú Cá Nhân` for the last section).

One `Edit` call per section.

---

### Step 8 — Update header count

Update the bank header:
```
> 🗂️ N câu · 7 chủ đề
```
to reflect the new total.

---

### Step 9 — Clean up chunks

```python
import shutil
shutil.rmtree('data/chunks')
```

---

### Step 10 — Verify

```powershell
Select-String -Pattern "^\*\*Câu" "Notes\Ngân Hàng Câu Hỏi Trắc Nghiệm CNTT.md" | Measure-Object | Select-Object Count
```

Count must match the number in the header.

---

## Notes

- The yellow-highlighted option **is** the correct answer — record it directly, no second-guessing
- If no highlight is visible on a question, read the next chunk before skipping
- Option letters may be randomised by the platform — trust the highlight position, not the letter
- Image too small to read → increase chunk size to 1600 px and re-slice
