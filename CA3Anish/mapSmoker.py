import sys
import csv

for line in sys.stdin:
    if line.startswith("age"):
        continue
    row = line.strip().split(",")
    try:
        smoker_status = row[4].strip().lower()
        if smoker_status == "yes":
            print(f"smoker\t1")
        elif smoker_status == "no":
            print(f"non-smoker\t1")
    except IndexError:
        continue
