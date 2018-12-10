import re

input = "input.in"
file = open(input, "r")
regex = r"position=<\s*(-?\d+),\s*(-?\d+)>\s*velocity=<\s*(-?\d+),\s*(-?\d+)>"

p = []

for line in file:
	matches = re.finditer(regex, line)
	m = re.match(regex, line)
	x = int(m.group(1))
	y = int(m.group(2))
	vx = int(m.group(3))
	vy = int(m.group(4))
	p.append([x,y,vx,vy])

bb = 10000000
while bb > 100 * 10:
	mi_x = 10000000
	ma_x = -10000000
	mi_y = 10000000
	ma_y = -10000000
	for i in range(len(p)):
		p[i][0] += p[i][2]
		p[i][1] += p[i][3]
		mi_x = min(mi_x, p[i][0])
		ma_x = max(ma_x, p[i][0])
		mi_y = min(mi_y, p[i][1])
		ma_y = max(ma_y, p[i][1])
	bb = (ma_x - mi_x) * (ma_y - mi_y)
	
grid = [["." for _ in range((ma_x - mi_x)+1)] for _ in range((ma_y - mi_y)+1)]
for x,y,_,_ in p:
	grid[y - mi_y][x - mi_x] = "#"

for i in range(len(grid)):
	print("".join(grid[i]))
		
