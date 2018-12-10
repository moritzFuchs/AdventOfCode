from collections import defaultdict
import re 

input = "input.in"
file = open(input, "r")

regex = r"#(\d+)\s@\s(\d+),(\d+)\:\s(\d+)x(\d+)"
n = 1000

grid = [[0 for _ in range(n)] for _ in range(n)]
total = 0

for line in file:
	matches = re.finditer(regex, line)
	m = re.match(regex, line)
	id = int(m.group(1))
	startX = int(m.group(2))
	startY = int(m.group(3))
	width = int(m.group(4))
	height = int(m.group(5))

	for j in range(startY, startY + height):
		for i in range(startX, startX + width):
			grid[i][j] += 1
			if grid[i][j] == 2:
				total += 1

#print(grid)

print(total)



