input = "input.in"
file = open(input, "r")

serialNumber = 7803
#serialNumber = 42 # 30
#serialNumber = 18 # 29
#print(getPowerLevel(122,79, 57))
#print(getPowerLevel(217,196, 39))
#print(getPowerLevel(101,153, 71))

def getPowerLevel(x,y, serialNumber):
	rackId = x+10
	level = (serialNumber + y * rackId) * rackId
	return int(str(level)[-3])-5

level = [[0 for _ in range(301)]for _ in range(301)]

for x in range(1,301):
	for y in range(1,301):
		level[x][y] = getPowerLevel(x,y,serialNumber)

sums = {}
for x in range(1,301):
	for y in range(1,301):
		sums[(x,y)] = level[x][y] + sums.get((x-1,y),0) + sums.get((x,y-1),0) - sums.get((x-1,y-1),0)
ma = -1000000000000
res = (-1,-1)
for x in range(1,301):
	for y in range(1,301):
		for width in range(1, 301 - max(x,y)):
			totalLevel = sums.get((x+width-1,y+width-1),0) 
			totalLevel -= sums.get((x-1,y+width-1),0) 
			totalLevel -= sums.get((x+width-1,y-1),0) 
			totalLevel += sums.get((x-1,y-1),0)
			if totalLevel > ma:
				ma = totalLevel
				res = (x,y,width) # For some reason I'm off by 1

print(res, ma)