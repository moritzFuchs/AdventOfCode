import string
from collections import deque, defaultdict

input = "input.in"
file = open(input, "r")

def getBest(points, x, y):
	res = -1
	dist = 1000000000
	for i in range(len(points)):
		x1,y1 = points[i]
		if abs(x-x1) + abs(y-y1) == dist:
			res = -1
		elif abs(x-x1) + abs(y-y1) < dist:
			dist = abs(x-x1) + abs(y-y1)
			res = i
	return res

ma_x = 0
ma_y = 0
mi_x = 0
mi_y = 0

points = []
for line in file:
	x,y = map(int, line.split(", "))
	points.append((x,y))
	ma_x = max(x,ma_x)
	mi_x = min(x,mi_x)
	ma_y = max(y,ma_y)
	mi_y = min(y,mi_y)

rem = set()
count = [0 for _ in range(len(points))]

for x in range(mi_x, ma_x+1):
	for y in range(mi_y, ma_y+1):
		who = getBest(points, x,y)
		if who == -1: continue
		count[who] += 1
		if x in [mi_x, ma_x] or y in [mi_y, ma_y]:
			rem.add(who)

for a in rem:
	count[a] = 0
print(max(count))
