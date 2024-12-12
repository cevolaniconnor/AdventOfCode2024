import re 

file = "day3puzzle.txt"
word = r'mul\(\d+,\d+\)'
total = 0

with open(file, 'r') as f:
	content = f.read()

matches = re.findall(word, content)

for match in matches:
	numbers = re.findall(r'\d+', match)
	for i in range(len(numbers)):
		# Converts each element to an integer
		numbers[i] = int(numbers[i])

		mult = numbers[0] * numbers[1]

	total += mult

print(total)


f.close()