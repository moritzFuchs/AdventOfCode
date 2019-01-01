from collections import defaultdict

def isAttackPossible(state, currentPos, gob):
	r,c = currentPos[0], currentPos[1]
	enemy = "G"
	if gob:
		enemy = "E"
	return state[r-1][c] == enemy or state[r+1][c] == enemy or state[r][c-1] == enemy or state[r][c+1] == enemy
	
def bestMove(currentPos, state, gob):
	q = [currentPos]
	seen = set(currentPos)
	dist = defaultdict(int)

	viablePositions = []

	while q:
		r,c = q.pop(0)
		for xd in [-1,0,1]:
			for yd in [-1,0,1]:
				if abs(xd) + abs(yd) == 1:
					np = (r+xd,c+yd)
					if np not in seen and state[np] == ".":
						dist[np] = dist[(r,c)]+1
						seen.add(np)
						q.append(np)
						if isAttackPossible(state, np, gob):
							viablePositions.append((np,dist[np]))
	if viablePositions:
		return sorted(viablePositions)[0]
	return (currentPos, -1)


input = "input.in"
file = open(input, "r")

state = defauldict(lambda: "#")
players = []

row = 0
for line in file:
	for col in range(len(line)):
		pos = (row, col)
		state[pos] = line[col]
		if line[col] == "G" or line[col] == "E":
			players.append((pos, line[col]))
	row += 1

players.sort()

print(players)
