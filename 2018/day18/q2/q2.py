from __future__ import print_function
from collections import defaultdict

def printState(state, rows, cols):
	print()
	for r in range(rows):
		for c in range(cols):
			print(state[r,c], end="")
		print()
	print()

input = "input.in"
file = open(input, "r")

state = []
rows = 0
for line in file:
	rows += 1
	state.append([x for x in line.strip()])

cols = len(state[0])
target = 1000000000

res = ""
num = 0
hashes = []
for num in range(1,1000):
	num += 1
	ns = defaultdict(lambda:"x")
	h = ""
	ns = [[x for x in y] for y in state]
	for r in range(rows):
		for c in range(cols):
			count = defaultdict(int)
			for dr in range(-1,2):
				for dc in range(-1,2):
					if dr == 0 and dc == 0: continue
					if 0 <= r+dr < rows and 0 <= c+dc < cols:
						count[state[r+dr][c+dc]] += 1
			if state[r][c] == "." and count["|"] >= 3:
				ns[r][c] = "|"
			elif state[r][c] == "|" and count["#"] >= 3:
				ns[r][c] = "#"
			elif state[r][c] == "#" and (count["#"] < 1 or count["|"] < 1):
				ns[r][c] = "."

	h = ''.join(''.join(row) for row in ns)
	if h in hashes:
		idx = hashes.index(h)
		hashes = hashes[hashes.index(h):]
		loopSize = len(hashes)
		
		res = hashes[(target - idx-1) % loopSize]
		break;
	
	hashes.append(h)
	state = ns

a,b = 0,0
for x in res:
	a += x == "#"
	b += x == "|"
r = a * b
print(r)
