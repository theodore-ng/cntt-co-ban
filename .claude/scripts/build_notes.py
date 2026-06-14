"""
Build one Obsidian note per video from VTT subtitle files.

Configure the constants below for each new playlist, then run:
    python build_notes.py

Output: one .md file per video in NOTES_DIR.
The merge step (merge_notes.py) consolidates them into 4 part notes.
"""

import re
import os
import glob

# ── Configure for each new playlist ──────────────────────────────────────────

TRANSCRIPTS_DIR = r"d:\Dev n Code\CNTT co ban\transcripts"
NOTES_DIR       = r"d:\Dev n Code\CNTT co ban\Notes\Word lecture"
LECTURE_NAME    = "Word lecture"

# (video_id, "Bài N", "Lesson title")  — in lesson order (Bài 1 first)
VIDEO_MAP = [
    ("rHUXRgKF9q0", "Bài 1",  "Các Thiết Lập Mặc Định"),
    ("GTHuO8VZ_A0", "Bài 2",  "Các Thao Tác Cơ Bản Khi Bắt Đầu Soạn Thảo"),
    ("kR_-5lvfVps", "Bài 3",  "Các Thao Tác Định Dạng Đoạn Văn Bản"),
    ("XU6TLIH1RQ4", "Bài 4",  "Định Dạng Bullets and Numbering"),
    ("fDnC9vpuvAM", "Bài 5",  "Sử Dụng Tab Tạo Văn Bản Dạng Cột"),
    ("7TVFB3UCYP0", "Bài 6",  "Sử Dụng Tab Tạo Văn Bản Dạng Biểu Mẫu (Form)"),
    ("Np7gMBQ-oCI", "Bài 7",  "Định Dạng Kẻ Khung và Tô Nền (Border and Shading)"),
    ("DnSve1jZpn0", "Bài 8",  "Tạo và Định Dạng Font Chữ Nghệ Thuật (WordArt)"),
    ("T6cAt0_AzJY", "Bài 9",  "Định Dạng Column và Dropcap"),
    ("eihxkppPGlc", "Bài 10", "Tạo và Định Dạng Picture"),
    ("wJkmpaJwLMQ", "Bài 11", "Thao Tác với Văn Bản Con (Textbox)"),
    ("_jPKPlQYOFA", "Bài 12", "Thao Tác với Đối Tượng Hình Vẽ (Shape)"),
    ("ia2NqotI6B0", "Bài 13", "Tạo và Định Dạng Bảng Table"),
    ("CHh5k2wNpCk", "Bài 14", "Các Thao Tác Định Dạng Bảng Table"),
    ("CpbFvzXmffA", "Bài 15", "Cách Tạo Công Thức Toán Học"),
]

# ─────────────────────────────────────────────────────────────────────────────


def parse_vtt(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    blocks = re.split(r'\n{2,}', content.strip())
    seen, lines = set(), []
    for block in blocks:
        for line in block.strip().splitlines():
            line = line.strip()
            if not line or line.startswith(("WEBVTT", "Kind:", "Language:")):
                continue
            if re.match(r'^\d+$', line) or re.match(r'^\d{2}:\d{2}', line):
                continue
            clean = re.sub(r'<[^>]+>', '', line).strip()
            if clean and clean not in seen:
                seen.add(clean)
                lines.append(clean)
    return lines


def segment_transcript(lines):
    raw = re.sub(r' {2,}', ' ', " ".join(lines))
    words = raw.split()
    paragraphs, chunk, count = [], [], 0
    for word in words:
        chunk.append(word)
        count += 1
        if count >= 40 and word[-1] in 'ahngciuym':
            paragraphs.append(" ".join(chunk))
            chunk, count = [], 0
    if chunk:
        paragraphs.append(" ".join(chunk))
    return "\n\n".join(paragraphs)


def slugify(text):
    text = text.lower()
    for pat, rep in [
        (r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a'), (r'[èéẹẻẽêềếệểễ]', 'e'),
        (r'[ìíịỉĩ]', 'i'), (r'[òóọỏõôồốộổỗơờớợởỡ]', 'o'),
        (r'[ùúụủũưừứựửữ]', 'u'), (r'[ỳýỵỷỹ]', 'y'), (r'[đ]', 'd'),
    ]:
        text = re.sub(pat, rep, text)
    text = re.sub(r'[^a-z0-9\-]', '-', text)
    return re.sub(r'-+', '-', text).strip('-')


def build_note(bai_num, bai_label, bai_title, transcript, video_id, prev_label, next_label):
    yt_url = f"https://www.youtube.com/watch?v={video_id}"
    nav_parts = []
    if prev_label:
        nav_parts.append(f"← [[{LECTURE_NAME} {prev_label}]]")
    nav_parts.append(f"[[{LECTURE_NAME}|📋 Mục lục]]")
    if next_label:
        nav_parts.append(f"[[{LECTURE_NAME} {next_label}]] →")
    nav = "  |  ".join(nav_parts)
    slug = slugify(bai_title)

    return f"""---
title: "Microsoft Word - {bai_label}: {bai_title}"
tags:
  - word
  - cntt-co-ban
  - {slug}
source: "{yt_url}"
---

# {bai_label}: {bai_title}

{nav}

> [!info] Nguồn
> 📺 [YouTube – {bai_label}: {bai_title}]({yt_url})
> 📚 [[{LECTURE_NAME}|Xem toàn bộ {LECTURE_NAME}]]

---

## Nội Dung Bài Học

> *Bản ghi được tổng hợp từ phụ đề tự động của video. Một số từ có thể bị nhận dạng sai do giọng nói.*

{transcript}

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


def main():
    os.makedirs(NOTES_DIR, exist_ok=True)

    all_vtts = sorted(glob.glob(os.path.join(TRANSCRIPTS_DIR, "*.vi.vtt")))
    vtt_by_bai = {}
    for path in all_vtts:
        m = re.search(r'[Bb][àa]i?\s*(\d+)', os.path.basename(path), re.IGNORECASE)
        if m:
            vtt_by_bai[int(m.group(1))] = path

    print(f"Matched VTTs: {sorted(vtt_by_bai.keys())}")

    for i, (vid_id, bai_label, bai_title) in enumerate(VIDEO_MAP):
        bai_num = i + 1
        vtt_path = vtt_by_bai.get(bai_num)
        if not vtt_path:
            print(f"  WARNING: no VTT for {bai_label}")
            transcript = "> ⚠️ Không tìm thấy file phụ đề cho bài này."
        else:
            transcript = segment_transcript(parse_vtt(vtt_path))

        content = build_note(
            bai_num, bai_label, bai_title, transcript, vid_id,
            prev_label=VIDEO_MAP[i-1][1] if i > 0 else None,
            next_label=VIDEO_MAP[i+1][1] if i < len(VIDEO_MAP)-1 else None,
        )
        filename = f"{LECTURE_NAME} {bai_label} - {bai_title}.md"
        with open(os.path.join(NOTES_DIR, filename), "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Created: {filename}")


if __name__ == "__main__":
    main()
