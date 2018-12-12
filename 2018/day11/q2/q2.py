from collections import defaultdict
serialNumber = 7803

def getPowerLevel(x,y, serialNumber):
	rackId = x+10
	level = (serialNumber + y * rackId) * rackId
	return int(str(level)[-3])-5

level = {}
for x in range(1,301):
	for y in range(1,301):
		level[(x,y)] = getPowerLevel(x,y,serialNumber)

sums = defaultdict(int)
for x in range(1,301):
	for y in range(1,301):
		sums[(x,y)] = level[(x,y)] + sums[(x-1,y)] + sums[(x,y-1)] - sums[(x-1,y-1)]
ma = -1000000000000
res = (-1,-1)
for x in range(1,301):
	for y in range(1,301):
		for width in range(1, 301 - max(x,y)):
			totalLevel = sums[(x+width-1,y+width-1)]
			totalLevel -= sums[(x-1,y+width-1)]
			totalLevel -= sums[(x+width-1,y-1)]
			totalLevel += sums[(x-1,y-1)]
			if totalLevel > ma:
				ma = totalLevel
				res = (x,y,width)

print(res, ma)