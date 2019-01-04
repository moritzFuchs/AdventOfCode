from collections import defaultdict
import re
import networkx 

def distance(bot1, bot2):
	res = 0
	for i in range(3):
		res += abs(bot1[i] - bot2[i])
	return res

input = "input.in"
file = open(input, "r")

regex = r"pos=<([-]?\d+),([-]?\d+),([-]?\d+)>,\sr=(\d+)"
center = (0,0,0)

lineSegs = []
bots = []
#g = networkx.Graph()
for line in file:
	matches = re.finditer(regex, line)
	m = re.match(regex, line)
	x = int(m.group(1))
	y = int(m.group(2))
	z = int(m.group(3))
	r = int(m.group(4))
	nb = (x,y,z,r)

	dist = distance(center, nb)

	lineSegs.append((dist-r,1))
	lineSegs.append((dist+r+1,0))

	#for bot in bots:
#		if distance(bot, nb) <= r + bot[3]:
#			g.add_edge(bot,nb)
#			g.add_edge(nb,bot)

	bots.append(nb)
lineSegs.sort()

print(lineSegs)

# Let's try to abuse the input instead of coding an octree..
res = 0
c = 0
maxC = 0
for d,t in lineSegs:
	if t == 1:
		c += 1
		if c > maxC:
			maxC = c
			res = d
	else:
		c -= 1

print(res)
# 125532606 too low

# Let's try a graph/clique approach.
#cl = max(list(networkx.find_cliques(g)), key=len)
#print(max([distance(center, bot) - bot[3] for bot in cl]))

# 125532606 too low


def intersect_count(box):
	res = 0
	for bot in bots:
		# get manhattan distance from bot to box
		d = 0
		for i in (0, 1, 2):
		    boxlow, boxhigh = box[0][i], box[1][i] - 1
		    d += abs(bot[i] - boxlow) + abs(bot[i] - boxhigh)
		    d -= boxhigh - boxlow
		d //= 2
		if d <= bot[3]:
			res += 1
	return res




