from collections import defaultdict

m = {"N":(-1,0),"S":(1,0),"W":(0,-1),"E":(0,1)}

def scan(input, stack, dist):
	res = []
	nstack = [x for x in stack]
	while len(input) > 0:
		x = input.pop(0)
		if x == ")":
			return (input, nstack)
		elif x == "(":
			input, nstack = scan(input, nstack, dist)
		elif x == "|":
			res += nstack
			nstack = [x for x in stack]
		else:
			nns = []
			for pos in nstack:
				np = (pos[0] + m[x][0],pos[1] + m[x][1])
				nns.append(np)
				dist[np] = min(dist[np], dist[pos]+1)
				#print(np, x, dist[np])
			nstack = nns
	res += nstack
	return input, res

input = "input.in"
file = open(input, "r")

for line in file:
	dist = defaultdict(lambda:100000000)
	dist[(0,0)] = 0
	_, stack = scan([x for x in line][1:-2], [(0,0)], dist)
	#print(dist)
	print(max(dist.values()))
	#exit(0)
	# part 2
	res = 0
	for x in dist.values():
		if x >= 1000 and x != 100000000:
			res += 1
	print(res)
 