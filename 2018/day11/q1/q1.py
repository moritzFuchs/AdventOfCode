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

totalLevel = [[0 for _ in range(301)]for _ in range(301)]

for x in range(1,300):
	for y in range(1,300):
		level = getPowerLevel(x,y,serialNumber)
		for i in [-1,0,1]:
			for j in [-1,0,1]:
				totalLevel[x+i][y+j] += level

res = -100000000000
resCo = (-1,-1)
for x in range(2,299):
	for y in range(2,299):
		if totalLevel[x][y] > res:
			res = totalLevel[x][y]
			resCo = (x-1, y-1)

print(res)
print(resCo)
