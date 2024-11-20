# # 1.	Using the Harry Potter.txt file, find which word in the document is the longest?


# Mapper: longest_word_mapper.py
# Mapper: longest_word_mapper.py
import sys
import re

pattern = re.compile(r'\W+') 

for line in sys.stdin:
    line = line.strip()
    words = pattern.sub(' ', line).split()
    for word in words:
        print(f"{word}\t{len(word)}")
