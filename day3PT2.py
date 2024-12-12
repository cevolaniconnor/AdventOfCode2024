import re 

file = "day3puzzle.txt"
word = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
total = 0
mult = 0

with open(file, 'r') as f:
	content = f.read().strip()

matches = re.findall(word, content)

g = True

for match in matches:
	if match == "do()":
		g = True
	elif match == "don't()":
		g = False
	else:
		if g:
			if match.startswith("mul"):
			# Extract numbers from the mul() function
				numbers = list(map(int, re.findall(r'\d+', match)))
				if len(numbers) == 2:
					result = numbers[0] * numbers[1]
					total += result

print(total)
