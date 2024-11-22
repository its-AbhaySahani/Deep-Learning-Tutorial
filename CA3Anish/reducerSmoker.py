import sys

counts = {"smoker": 0, "non-smoker": 0}

for line in sys.stdin:
    try:
        key, count = line.strip().split("\t")
        count = int(count)
        if key in counts:
            counts[key] += count
    except ValueError:
        continue

for key, count in counts.items():
    print(f"{key}: {count}")
