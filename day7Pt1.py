from itertools import product
from tqdm import tqdm

file = "day7Puzzle.txt"
with open(file) as f:
	content = f.read().strip().split("\n")

total = 0

for i, line in enumerate(content):
	piece = line.split()
	target = int(piece[0][:-1])
	numbers = list(map(int, piece[1:]))


	def check(combo):
		total = numbers[0]

		for i in range(1, len(numbers)):
			if combo[i -1] == "+":
				total += numbers[i]
			else:
				total *= numbers[i]
		return total

	for combo in product("*+|", repeat=len(numbers)-1):
		if check(combo) == target:
			total += target
			break

print(total)
