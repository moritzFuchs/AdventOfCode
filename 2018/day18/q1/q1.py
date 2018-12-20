from collections import defaultdict

input = "input.in"
file = open(input, "r")

state = defaultdict(lambda:"x")
rows = 0
cols = 0
for line in file:
	cols = max(cols, len(line))
	for col in range(len(line)):
		state[rows,col] = line[col]
	rows += 1

for _ in range(10):
	ns = defaultdict(lambda:"x")
	for r in range(rows):
		for c in range(cols):
			count = defaultdict(int)
			for dr in range(-1,2):
				for dc in range(-1,2):
					if dr == 0 and dc == 0: continue
					count[state[r+dr,c+dc]] += 1
			if state[r,c] == "." and count["|"] >= 3:
				ns[r,c] = "|"
			elif state[r,c] == "|" and count["#"] >= 3:
				ns[r,c] = "#"
			elif state[r,c] == "#" and (count["#"] < 1 or count["|"] < 1):
				ns[r,c] = "."
			else:
				ns[r,c] = state[r,c]
	state = ns

a,b = 0,0
for r in range(rows):
	for c in range(cols):
		if state[r,c] == "#":
			a += 1
		elif state[r,c] == "|":
			b += 1
print(a*b)
