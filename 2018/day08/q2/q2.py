input = "sample.in"
file = open(input, "r")

def doIt(inp):
	total = 0
	nc = inp[0]
	mc = inp[1]
	
	inp = inp[2:]
	if nc == 0:
		idx = 0
		for _ in range(mc):
			total += inp[idx]
			idx += 1
		return total, inp[idx:]
	else:
		v = defaultdict(int)
		for i in range(nc):
			t, inp = doIt(inp)
			v[i+1] = t
		
		idx = 0
		for _ in range(mc):
			total += v[inp[idx]]
			idx += 1
	
	return (total, inp[idx:])

for line in file:
	print(doIt(list(map(int, line.split())))[0])
