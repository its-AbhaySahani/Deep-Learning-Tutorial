#2.	Calculate the average BMI of all individuals in the insurance.csv dataset.

# Reducer: average_bmi_reducer.py
import sys

total_bmi = 0
total_count = 0

for line in sys.stdin:
    try:
        bmi, count = line.strip().split("\t")
        bmi = float(bmi)
        count = int(count)
        total_bmi += bmi
        total_count += count
    except ValueError:
        continue

if total_count > 0:
    average_bmi = total_bmi / total_count
    print(f"Average BMI: {average_bmi:.2f}")
else:
    print("No valid BMI data found.")
