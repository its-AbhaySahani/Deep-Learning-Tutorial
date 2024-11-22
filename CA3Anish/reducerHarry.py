import sys

total_count = 0

for line in sys.stdin:
    try:
        word, count = line.strip().split('\t')
        count = int(count)
        if word == 'Romeo':
            total_count += count
    except ValueError:
        continue

print(f"The word 'Romeo' appears {total_count} times.")
