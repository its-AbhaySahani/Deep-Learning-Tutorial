# 2.	Calculate the average BMI of all individuals in the insurance.csv dataset.
# using map and reduce functions
# Mapper: average_bmi_mapper.py
import sys
import csv

for line in sys.stdin:
    if line.startswith("age"):
        continue
    
    row = line.strip().split(",")
    
    try:
        bmi = float(row[2])
    
        print(f"{bmi}\t1")
    except ValueError:
        continue

