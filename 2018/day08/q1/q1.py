input = "input.in"
file = open(input, "r")

def doIt(inp):
	total = 0
	nc = inp[0]
	mc = inp[1]
	
	inp = inp[2:]
	for _ in range(nc):
		t, inp = doIt(inp)
		total += t
	
	idx = 0
	for _ in range(mc):
		total += inp[idx]
		idx += 1
	
	return (total, inp[idx:])

for line in file:
	print(doIt(list(map(int, line.split())))[0])