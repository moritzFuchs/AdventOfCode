from collections import defaultdict
import heapq
import os
from time import sleep
import copy

def printField(state):
	for row in range(len(state)):
		add = []
		for col in range(len(state[row])):
			if state[row][col] in ["G", "E"]:
				add.append(str(hitpoints[row][col]))
		print("".join(state[row]), end="")
		print("    ", end="")
		print(" ".join(add))
		
def copyState(state):
	ns = []
	for row in range(len(state)):
		ns.append([])
		for col in range(len(state[row])):
			ns[-1].append(state[row][col])
	return ns

def isAttackPossible(state, currentPos, enemy):
	r,c = currentPos[0], currentPos[1]
	return state[r-1][c] == enemy or state[r+1][c] == enemy or state[r][c-1] == enemy or state[r][c+1] == enemy

def getField(state, pos):
	return state[pos[0]][pos[1]]

def searchNextEnemies(state, currentPos, debug=False):
	enemy = "E"
	if getField(state, currentPos) == "E":
		enemy = "G"
	res = []
	seen = set()
	seen.add(currentPos)
	
	q = [(0, currentPos)]
	while q:
		dist, pos = heapq.heappop(q)
		if isAttackPossible(state, pos, enemy):
			res.append(pos)
			while q:
				dist2, pos2 = heapq.heappop(q)
				if dist != dist2:
					return res, dist
				if isAttackPossible(state, pos2, enemy):
					res.append(pos2)
			return res, dist

		for dx in range(-1,2):
			for dy in range(-1,2):
				if abs(dx) + abs(dy) == 1:
					newPos = (pos[0]+dx, pos[1]+dy)
					if newPos not in seen and getField(state, newPos) == ".":
						heapq.heappush(q,(dist+1, newPos))
						seen.add(newPos)
	return [], -1

def manhattan(p1,p2):
	res = 0
	for i in range(2):
		res += abs(p1[i] - p2[i])
	return res

def searchNextMove(state, targetPos, playerPos):
	res = []
	seen = set()
	seen.add(targetPos)
	q = [(0, targetPos)]
	while q:
		dist, pos = heapq.heappop(q)
		if manhattan(playerPos, pos) == 1:
			res.append(pos)
			while q:
				dist2, pos2 = heapq.heappop(q)
				if dist != dist2:
					return res, dist
				if manhattan(playerPos, pos2) == 1:
					res.append(pos2)
			return res, dist
		for dx in range(-1,2):
			for dy in range(-1,2):
				if abs(dx) + abs(dy) == 1:
					newPos = (pos[0]+dx, pos[1]+dy)
					if newPos not in seen and getField(state, newPos) == ".":
						heapq.heappush(q,(dist+1, newPos))
						seen.add(newPos)		

def getAdjacentEnemies(state, pos):
	enemy = "E" if getField(state, pos) == "G" else "G"
	r,c = pos[0], pos[1]
	res = []
	if state[r-1][c] == enemy:
		res.append((hitpoints[r-1][c],(r-1,c)))
	if state[r+1][c] == enemy:
		res.append((hitpoints[r+1][c],(r+1,c)))
	if state[r][c-1] == enemy:
		res.append((hitpoints[r][c-1],(r,c-1)))
	if state[r][c+1] == enemy:
		res.append((hitpoints[r][c+1],(r,c+1)))
	return res

def setField(state, pos, value):
	state[pos[0]][pos[1]] = value

def gameOver(state):
	gs,es = 0,0
	for x in state:
		for y in x:
			gs += y == "G"
			es += y == "E"
	return (gs == 0 or es == 0)

attackPower = 3

input_file = "sample.in" # 4988
#input_file = "sample2.in" # 36334
#input_file = "sample3.in" # 39514
#input_file = "sample4.in" # 27755
#input_file = "sample5.in" # 28944
#input_file = "sample6.in" # 18740
input_file = "input.in" # ?
file = open(input_file, "r")

startState = []
startHitpoints = []
startPlayers = []

row = 0
for line in file:
	line = line.strip()
	startState.append([])
	startHitpoints.append([])
	for col in range(len(line)):
		pos = (row, col)
		if line[col] == "G" or line[col] == "E":
			startPlayers.append(pos)
			startHitpoints[-1].append(200)
		else:
			startHitpoints[-1].append(-1)
		startState[-1].append(line[col])
	row += 1

clear = lambda: os.system('cls')
clear()

elfAttack = 3
while True:
	state = copy.deepcopy(startState)
	hitpoints = copy.deepcopy(startHitpoints)
	players = copy.deepcopy(startPlayers)

	elfAttack += 1

	rounds = 0
	printField(state)
	stop = False
	while not gameOver(state):
		players.sort()
		np = []	
		skip = set()
		for player in players:
			if player in skip: # player must be dead
				continue

			skip.add(player)
			if not isAttackPossible(state, player, "E" if getField(state, player) == "G" else "G"):
				targets, dist = searchNextEnemies(state, player, player == (5, 7))
				if dist > 0:
					target = min(targets)

					starts, dist = searchNextMove(state, target, player)
					move = min(starts)
					
					skip.add(move)

					hitpoints[move[0]][move[1]] = hitpoints[player[0]][player[1]]
					hitpoints[player[0]][player[1]] = -1

					setField(state, move, getField(state, player))
					setField(state, player, ".")


					player = move
			enemies = getAdjacentEnemies(state, player)
			if len(enemies) > 0:
				_, enemyPos = min(enemies)
				hitpoints[enemyPos[0]][enemyPos[1]] -= elfAttack if getField(state, player) == "E" else attackPower
				if hitpoints[enemyPos[0]][enemyPos[1]] <= 0:
					if getField(state, enemyPos) == "E":
						stop = True
						break
					skip.add(enemyPos)
					if enemyPos in np:
						np.remove(enemyPos)
					setField(state, enemyPos, ".")
					hitpoints[enemyPos[0]][enemyPos[1]] = -1
					if gameOver(state) and players[-1] != player:
						total = 0
						for x in hitpoints:
							for y in x:
								if y > 0:
									total += y
						print(rounds, total, total * rounds)
						exit(0)

			np.append(player)
		if stop:
			break
		clear()
		print("Round {}".format(rounds+1))
		print("Elfattack {}".format(elfAttack))
		printField(state)
		players = np
		sleep(0.05)
		rounds += 1
		#input()


total = 0
for x in hitpoints:
	for y in x:
		if y > 0:
			total += y
print(rounds, total, total * rounds)
exit(0)