from collections import defaultdict
import re 

input = "input.in"
file = open(input, "r")

regex = r"#(\d+)\s@\s(\d+),(\d+)\:\s(\d+)x(\d+)"
n = 1000

grid = [[0 for _ in range(n)] for _ in range(n)]
total = 0

tmp = []

for line in file:
	matches = re.finditer(regex, line)
	m = re.match(regex, line)
	idx = int(m.group(1))
	startX = int(m.group(2))
	startY = int(m.group(3))
	width = int(m.group(4))
	height = int(m.group(5))
	tmp.append((idx,startX,startY,width,height))

	overlap = 0
	for j in range(startY, startY + height):
		for i in range(startX, startX + width):
			grid[i][j] += 1
			
# yikes... there must be a better way of doing this..
for idx,  startX, startY, width, height in tmp:
	stop = False 
	for j in range(startY, startY + height):
		for i in range(startX, startX + width):
			if grid[i][j] > 1:
				stop = True
				break;
		if stop: break;
	if not stop:
		print(idx)
		exit(0)
