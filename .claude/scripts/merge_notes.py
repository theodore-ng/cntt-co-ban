"""
Merge individual per-video notes into 4 grouped part notes + an index note.

Run AFTER build_notes.py. Configure PARTS and NOTES_DIR below, then:
    python merge_notes.py
"""

import re
import os
import glob

# ── Configure for each new playlist ──────────────────────────────────────────

NOTES_DIR    = r"d:\Dev n Code\CNTT co ban\Notes\Word lecture"
LECTURE_NAME = "Word lecture"
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLAHEk62D9lz94N_L2mqV6lAlYVBIhNNFz"

# (video_id, "Bài N", "Lesson title") — same order as build_notes.py
VIDEO_MAP = {
    1:  ("rHUXRgKF9q0", "Bài 1",  "Các Thiết Lập Mặc Định"),
    2:  ("GTHuO8VZ_A0", "Bài 2",  "Các Thao Tác Cơ Bản Khi Bắt Đầu Soạn Thảo"),
    3:  ("kR_-5lvfVps", "Bài 3",  "Các Thao Tác Định Dạng Đoạn Văn Bản"),
    4:  ("XU6TLIH1RQ4", "Bài 4",  "Định Dạng Bullets and Numbering"),
    5:  ("fDnC9vpuvAM", "Bài 5",  "Sử Dụng Tab Tạo Văn Bản Dạng Cột"),
    6:  ("7TVFB3UCYP0", "Bài 6",  "Sử Dụng Tab Tạo Văn Bản Dạng Biểu Mẫu (Form)"),
    7:  ("Np7gMBQ-oCI", "Bài 7",  "Định Dạng Kẻ Khung và Tô Nền (Border and Shading)"),
    8:  ("DnSve1jZpn0", "Bài 8",  "Tạo và Định Dạng Font Chữ Nghệ Thuật (WordArt)"),
    9:  ("T6cAt0_AzJY", "Bài 9",  "Định Dạng Column và Dropcap"),
    10: ("eihxkppPGlc", "Bài 10", "Tạo và Định Dạng Picture"),
    11: ("wJkmpaJwLMQ", "Bài 11", "Thao Tác với Văn Bản Con (Textbox)"),
    12: ("_jPKPlQYOFA", "Bài 12", "Thao Tác với Đối Tượng Hình Vẽ (Shape)"),
    13: ("ia2NqotI6B0", "Bài 13", "Tạo và Định Dạng Bảng Table"),
    14: ("CHh5k2wNpCk", "Bài 14", "Các Thao Tác Định Dạng Bảng Table"),
    15: ("CpbFvzXmffA", "Bài 15", "Cách Tạo Công Thức Toán Học"),
}

# Edit groupings to suit the playlist content
PARTS = [
    {
        "num": 1,
        "title": "Thiết Lập và Soạn Thảo Cơ Bản",
        "bai_range": range(1, 6),
        "desc": "Các bước thiết lập môi trường Word và kỹ năng soạn thảo nền tảng",
    },
    {
        "num": 2,
        "title": "Bố Cục và Định Dạng Nâng Cao",
        "bai_range": range(6, 10),
        "desc": "Tab, border, WordArt, column và các kỹ thuật trình bày trang",
    },
    {
        "num": 3,
        "title": "Đối Tượng và Hình Ảnh",
        "bai_range": range(10, 13),
        "desc": "Chèn và định dạng Picture, Textbox, Shape",
    },
    {
        "num": 4,
        "title": "Bảng và Công Thức",
        "bai_range": range(13, 16),
        "desc": "Tạo và định dạng bảng Table, công thức toán học",
    },
]

# ─────────────────────────────────────────────────────────────────────────────


def find_note(bai_num):
    files = glob.glob(os.path.join(NOTES_DIR, f"{LECTURE_NAME} Bài {bai_num} - *.md"))
    return files[0] if files else None


def extract_transcript(note_path):
    with open(note_path, encoding="utf-8") as f:
        content = f.read()
    m = re.search(r'## Nội Dung Bài Học\n+> \*.*?\*\n+(.*?)(?=\n---\n)', content, re.DOTALL)
    return m.group(1).strip() if m else ""


def nav_line(pnum, total):
    prev = f"← [[{LECTURE_NAME} - Phần {pnum-1}]]  |  " if pnum > 1 else ""
    nxt  = f"  |  [[{LECTURE_NAME} - Phần {pnum+1}]] →" if pnum < total else ""
    return f"{prev}[[{LECTURE_NAME}|📋 Mục lục]]{nxt}"


def build_part(part, total_parts):
    pnum, ptitle, pdesc = part["num"], part["title"], part["desc"]
    nav = nav_line(pnum, total_parts)

    sections = []
    for bai_num in part["bai_range"]:
        vid_id, bai_label, bai_title = VIDEO_MAP[bai_num]
        yt_url = f"https://www.youtube.com/watch?v={vid_id}"
        path = find_note(bai_num)
        transcript = extract_transcript(path) if path else "> ⚠️ Không tìm thấy phụ đề."
        sections.append(f"### {bai_label}: {bai_title}\n\n> 📺 [Xem video]({yt_url})\n\n{transcript}")

    body = "\n\n---\n\n".join(sections)

    return f"""---
title: "{LECTURE_NAME} - Phần {pnum}: {ptitle}"
tags:
  - word
  - cntt-co-ban
  - phan-{pnum}
---

# Phần {pnum}: {ptitle}

{nav}

> {pdesc}

---

{body}

---

## Ghi Chú Cá Nhân

> [!question] Câu hỏi / Điểm cần làm rõ
> -

> [!check] Đã nắm được
> -

> [!todo] Cần thực hành thêm
> -

---

{nav}
"""


def build_index(parts):
    table_rows = "\n".join(
        f"| [[{LECTURE_NAME} - Phần {p['num']}\\|Phần {p['num']}]] | {p['title']} | Bài {list(p['bai_range'])[0]}–{list(p['bai_range'])[-1]} |"
        for p in parts
    )
    checklist = ""
    for p in parts:
        checklist += f"\n### Phần {p['num']} — {p['title']}\n"
        for n in p["bai_range"]:
            _, lbl, title = VIDEO_MAP[n]
            checklist += f"- [ ] {lbl} — {title}\n"

    return f"""---
title: "{LECTURE_NAME} - Microsoft Word Cơ Bản"
tags:
  - word
  - cntt-co-ban
  - index
---

# {LECTURE_NAME} — Microsoft Word Cơ Bản

> 📺 [YouTube Playlist]({PLAYLIST_URL})
> 🗂️ {len(VIDEO_MAP)} bài · {len(parts)} phần

---

## Mục Lục

| Phần | Chủ đề | Bài |
|------|--------|-----|
{table_rows}

---

## Checklist Học Tập
{checklist}
---

> [!tip] Mẹo học hiệu quả
> Xem video → Đọc phần tương ứng → Thực hành trong Word → Tick checklist
"""


def main():
    # Remove individual notes
    deleted = sum(
        1 for n in range(1, len(VIDEO_MAP)+1)
        if (p := find_note(n)) and os.remove(p) is None
    )
    print(f"Deleted {deleted} individual notes.")

    total = len(PARTS)
    for part in PARTS:
        content = build_part(part, total)
        path = os.path.join(NOTES_DIR, f"{LECTURE_NAME} - Phần {part['num']}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Created: {os.path.basename(path)}")

    index_path = os.path.join(NOTES_DIR, f"{LECTURE_NAME}.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(build_index(PARTS))
    print(f"  Updated: {os.path.basename(index_path)}")


if __name__ == "__main__":
    main()
