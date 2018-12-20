from __future__ import print_function
from collections import defaultdict
import re
import sys
sys.setrecursionlimit(5000)

calls = 0

def search(state, y,x, d):
	state[y,x] = "|"
	if state[y,x+d] == "#":
		return True, y, x
	if state[y,x+d] in [".", "|"]:
		if state[y+1,x+d] in ["#", "w"]:
			return search(state, y,x+d, d)
		return False, y,x+d
	print(state[y,x], state[y,x+d],y,x,d)

def fillRow(state, y,xLeft, xRight):
	for x in range(xLeft, xRight+1):
		state[y,x] = "w"

def dropWater(state, y, x, depth=0):
	
	if state[y,x] == "w": return 
	if state[y+1,x] =="|":
		state[y,x] = "|"
		return

	if state[y+1,x] in ["#", "w"]:
		blockedLeft, yLeft,xLeft = search(state, y, x, -1)
		blockedRight, yRight,xRight = search(state, y, x, 1)
		if blockedLeft and blockedRight:
			fillRow(state, y,xLeft, xRight)
		else:
			if not blockedLeft:
				dropWater(state, yLeft, xLeft, depth+1)
			if not blockedRight:
				dropWater(state, yRight, xRight, depth+1)
	else:
		state[y,x] = "|"
		if y+1 <= maxy:
			dropWater(state, y+1,x, depth+1)
			dropWater(state, y, x, depth+1)

def printState(state, minY, maxY, minX, maxX):
	for y in range(minY, maxY+1):
		for x in range(minX, maxX+1):
			print(state[y,x], end="")
		print("")

input = "input.in"
file = open(input, "r")

regex = r"(x|y)=(\d+),\s(x|y)=(\d+)(\.\.)?(\d+)"

state = defaultdict(lambda: ".")
pos = defaultdict(int)
miny = 100000000000
maxy = 0
minx = 1000000000000
maxx = 0

for line in file:

	matches = re.finditer(regex, line)
	m = re.match(regex, line)
	id = m.group(1)
	val = int(m.group(2))
	pos[id] = val

	id2 = m.group(3)
	val2Start = int(m.group(4))
	val2End = int(m.group(4))
	if len(m.groups()) == 6:
		val2End = int(m.group(6))
	
	for v in range(val2Start, val2End+1):
		pos[id2] = v
		state[pos["y"],pos["x"]] = "#"
		
		maxy = max(maxy, pos["y"])
		maxx = max(maxx, pos["x"])

		miny = min(miny, pos["y"])
		minx = min(minx, pos["x"])

print(miny, maxy, minx, maxx)


source = 0,500
state[0,500] = "+"

printState(state, miny, maxy, minx-5, maxx+5)

dropWater(state, 1, 500)
print()
print()
printState(state, miny, maxy, minx-5, maxx+5)

res = 0
rem = 0
for y in range(miny, maxy+1):
	for x in range(minx-5, maxx+6):
		res += state[y,x] in ["w", "|"]
		rem += state[y,x] == "w"

print(res)
print(rem)
