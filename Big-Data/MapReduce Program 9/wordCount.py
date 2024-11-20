import sys
import re

WORD_RE = re.compile(r"\b\w+\b")

for line in sys.stdin:
    words = WORD_RE.findall(line.lower())
    for word in words:
        print(f"{word}\t1")


