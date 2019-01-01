from collections import defaultdict
import heapq

#depth = 510
#target = (10,10)

depth = 7305
target = (13,734)

equip = ['c', 't', 'n']

area = (target[0] + 100, target[1] + 100)
maxX = area[0] 
maxY = area[1]

def valid(t, equipment):
	if t == 0: # rocky
		return equipment in ['c', 't']
	elif t == 1: # wet 
		return equipment in ['c', 'n']
	elif t == 2: # narrow
		return equipment in ['t', 'n']

def getEquipmentNeighbors(current, el):
	res = []
	x,y,e = current
	for ne in equip:
		if ne != e and valid(el[x][y]%3, ne):
			res.append((x,y,ne))
	return res

def getWalkNeighbors(current, el):
	res = []
	x,y,e = current
	for dx in range(-1,2):
		for dy in range(-1,2):
			if abs(dx)+abs(dy) == 1 and 0 <= x+dx <= maxX and 0 <= y+dy <= maxY and valid(el[x+dx][y+dy]%3,e):
				res.append((x+dx,y+dy,e))
	return res

def erosion(x):
	return (x+depth)%20183

el = [[0 for _ in range(area[1]+1)] for _ in range(area[0]+1)]
risk = 0
for x in range(area[0]+1):
	for y in range(area[1]+1):

		if (x == 0 and y == 0) or (x == target[0] and y == target[1]):
			el[x][y] = erosion(0)
		elif x == 0:
			el[x][y] = erosion(y * 48271)
		elif y == 0:
			el[x][y] = erosion(x * 16807)
		else:			
			el[x][y] = erosion(el[x-1][y] * el[x][y-1])
		
done = set()
q = []
dist = defaultdict(lambda: 10000000000000)
dist[(0,0,'t')] = 0
heapq.heappush(q, (0,(0,0,'t')))

while q:
	d, current = heapq.heappop(q)
	if current[0] == target[0] and current[1] == target[1] and current[2] == 't':
		print("Done!")
		print(d)
		break
	if current in done:
		continue
	for neigh in getWalkNeighbors(current, el):
		if d+1 < dist[neigh]:
			dist[neigh] = d+1
			heapq.heappush(q, (d+1,neigh))
	for neigh in getEquipmentNeighbors(current, el):
		if d+7 < dist[neigh]:
			dist[neigh] = d+7
			heapq.heappush(q, (d+7,neigh))
	