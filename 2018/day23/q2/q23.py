from collections import defaultdict
import re
import heapq

def distance(bot1, bot2):
	res = 0
	for i in range(3):
		res += abs(bot1[i] - bot2[i])
	return res

def countBots(box):
	res = 0
	for bot in bots:
		# get manhattan distance from bot to box
		d = 0
		for i in range(3):
		    boxSegLeft = box[0][i]
		    boxSegRight = box[1][i] - 1

		    if bot[i] < boxSegLeft:
		    	d += boxSegLeft - bot[i]
		    elif boxSegRight < bot[i]:
		    	d += bot[i] - boxSegRight

		if d <= bot[3]:
			res += 1
	return res

input = "input.in"
file = open(input, "r")

regex = r"pos=<([-]?\d+),([-]?\d+),([-]?\d+)>,\sr=(\d+)"
center = (0,0,0)

lineSegs = []
bots = []
maxCord = 0

for line in file:
	matches = re.finditer(regex, line)
	m = re.match(regex, line)
	x = int(m.group(1))
	y = int(m.group(2))
	z = int(m.group(3))
	r = int(m.group(4))
	
	maxCord = max(abs(x)+r, maxCord)
	maxCord = max(abs(y)+r, maxCord)
	maxCord = max(abs(z)+r, maxCord)

	nb = (x,y,z,r)
	bots.append(nb)

# get starting box with convenient size = 2^?
size = 1
while size <= maxCord:
	size *= 2

cube_corners = [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
starting_box = ((-size,-size,-size),(size,size,size))
q = []
heapq.heappush(q, (-len(bots), -2*size, 100000000, starting_box))

i = 0
while q:
	_, size, dist, box = heapq.heappop(q)
	size *= -1
	if size == 1:
		print(dist)
		break

	newSize = size // 2
	for corner in cube_corners:
		newSmallCorner = [box[0][i] + corner[i] * newSize for i in range(3)]
		newLargeCorner = [newSmallCorner[i] + newSize for i in range(3)]
		newNBots = countBots((newSmallCorner, newLargeCorner))	
		heapq.heappush(q, (-newNBots, -newSize, distance(center, newSmallCorner), (newSmallCorner, newLargeCorner)))
	