# 1.	Using the Harry Potter.txt file, find which word in the document is the longest?

# Reducer: longest_word_reducer.py
import sys

max_length = 0
longest_word = ""

for line in sys.stdin:
    word, length = line.strip().split('\t')
    length = int(length)
    if length > max_length:
        max_length = length
        longest_word = word

print(f"Longest Word: {longest_word}, Length: {max_length}")
