# find how many times the word "Romeo" appears in the text
import sys

for line in sys.stdin:
    line = line.lower().strip()

    words = line.split()

    for word in words:
        if word == "romeo":
            print(f'{word}\t1')