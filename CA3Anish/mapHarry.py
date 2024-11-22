import re

# Define the regex pattern for splitting words
pattern = re.compile(r'\W+')

# Open the input file explicitly
with open('HarryPotter.txt', 'r') as f:
    for line in f:
        words = pattern.sub(' ', line.strip()).split()
        for word in words:
            if word.lower() == 'romeo':  # Match "Romeo" case-insensitively
                print(f"Romeo\t1")
