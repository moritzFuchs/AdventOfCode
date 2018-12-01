from collections import defaultdict
input = "sample.in"
#input = "input.in"


file = open(input, "r")

grid = []

for line in file:
    
    currentLine = []
    for c in line:
        if c != "\n":
            currentLine.append(c)
    grid.append(currentLine)


start = -1
for ind in range(len(grid[0])):
    if grid[0][ind] == '|':
        start = ind

direction = (-1,0)

currentPos = (0,start)

while True:
	nPos = (currentPos[0] + direction[0], currentPos[1] + direction[1])
	
	if nPos[0] >= len(grid) or nPos[0] < 0 or nPos[1] >= len(grid[0]) or nPos[1] < 0:
		break
	
	if grid[nPos[0]][nPos[1]] == "+":
		# switch direction
		if abs(direction[0]) == 1:
			if grid[nPos[0]][nPos[1]-1] != " ":
				direction = (-1,0)
			else:
				direction = (1,0)
		else:
			if grid[nPos[0]-1][nPos[1]] != " ":
				direction = (0,-1)
			else:
				direction = (0,1)
	currentPos = nPos

print(start)

print(grid)