import re 

file = "day4Puzzle.txt"
total = 0

with open(file, 'r') as f:
	content = f.read().strip()

row = len(content)
col = len(content[0])

for r in range(row):
	for c in range(col):
		