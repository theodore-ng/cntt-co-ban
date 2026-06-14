"""
Parse a YouTube VTT subtitle file into clean, deduplicated text lines.

Usage:
    python parse_vtt.py <path-to.vi.vtt>

Output: plain text to stdout (pipe to a file with Out-File -Encoding utf8).
"""

import re
import sys


def parse_vtt(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    blocks = re.split(r'\n{2,}', content.strip())
    seen = set()
    sentences = []

    for block in blocks:
        for line in block.strip().splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith(("WEBVTT", "Kind:", "Language:")):
                continue
            if re.match(r'^\d+$', line):
                continue
            if re.match(r'^\d{2}:\d{2}', line):
                continue
            # Remove inline timing tags: <00:00:01.280><c> word</c>
            clean = re.sub(r'<[^>]+>', '', line).strip()
            if clean and clean != ' ' and clean not in seen:
                seen.add(clean)
                sentences.append(clean)

    return sentences


def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_vtt.py <path-to.vi.vtt>", file=sys.stderr)
        sys.exit(1)
    for line in parse_vtt(sys.argv[1]):
        print(line)


if __name__ == "__main__":
    main()
