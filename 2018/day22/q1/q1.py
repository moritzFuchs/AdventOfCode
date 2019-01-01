from collections import defaultdict

#depth = 510
#target = (10,10)

depth = 7305
target = (13,734)

def erosion(x):
	return (x+depth)%20183

el = [[0 for _ in range(target[1]+1)] for _ in range(target[0]+1)]
risk = 0
for x in range(target[0]+1):
	for y in range(target[1]+1):

		if (x == 0 and y == 0) or (x == target[0] and y == target[1]):
			el[x][y] = erosion(0)
		elif x == 0:
			el[x][y] = erosion(y * 48271)
		elif y == 0:
			el[x][y] = erosion(x * 16807)
		else:			
			el[x][y] = erosion(el[x-1][y] * el[x][y-1])
		
		risk += el[x][y]%3
		#print(((gi[x][y] + depth) % 20183)%3, end="")
	#print("")
print(risk)