import string
from collections import deque, defaultdict

input = "input.in"
file = open(input, "r")

def getCumDist(points, x, y):
	res = 0
	for i in range(len(points)):
		x1,y1 = points[i]
		res += abs(x-x1) + abs(y-y1)
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
res = 0
# Technically wrong, but works if points are spread well
for x in range(mi_x, ma_x+1):
	for y in range(mi_y, ma_y+1):
		d = getCumDist(points, x,y)
		if d < 10000:
			res += 1
		
print(res)
