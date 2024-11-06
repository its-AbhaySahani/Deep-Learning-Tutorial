import sys

current_word = None
current_count = 0
max_word = None
max_count = 0

for line in sys.stdin:
    word, count = line.strip().split("\t")
    count = int(count)
    

    if current_word == word:
        current_count += count
    else:
        if current_word:
            if current_count > max_count:
                max_word = current_word
                max_count = current_count
        current_word = word
        current_count = count

if current_word:
    if current_count > max_count:
        max_word = current_word
        max_count = current_count

print(f"{max_word}\t{max_count}")