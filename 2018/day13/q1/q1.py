from collections import defaultdict
import heapq

input = "input.in"
file = open(input, "r")

def turnLeft(direction):
	if direction == "<":
		return "v"
	if direction == "v":
		return ">"
	if direction == ">":
		return "^"
	if direction == "^":
		return "<"

def turnRight(direction):
	#fuck it..
	return turnLeft(turnLeft(turnLeft(direction)))

field = defaultdict(lambda:" ")
rows = 0
cols = 0
for line in file:
	for col in range(len(line)):
		field[(rows,col)] = line[col]
		cols = max(cols, col)
	rows += 1
	
carts = []
turnCount = defaultdict(int)
cartCount = defaultdict(int)
cartid = 0
for row in range(rows):
	for col in range(cols):
		if field[(row,col)] in ["<",">","^","v"]:
			carts.append((row,col,field[(row,col)], cartid))
			cartid += 1
			cartCount[(row,col)] += 1
			top = field[(row-1,col)] in ["|", "\\", "/","+"]
			bottom = field[(row+1,col)] in ["|", "\\", "/","+"]
			left = field[(row,col-1)] in ["-", "\\", "/","+"]
			right = field[(row,col+1)] in ["-", "\\", "/","+"]
			if left and right and top and bottom:
				field[(row,col)] = "+"
			elif top and bottom:
				field[(row,col)] = "|"
			elif left and right:
				field[(row,col)] = "-"
			elif (left and top) or (right and bottom):
				field[(row,col)] = "/"
			elif (right and top) or (left and bottom):
				field[(row,col)] = "\\"

movement = {"<":(0,-1), ">":(0,1),"^":(-1,0), "v":(1,0)}
while True:
	nc = []
	for row,col,dire,cid in carts:
		mr, mc = movement[dire]
		cartCount[(row,col)] -= 1
		row += mr
		col += mc
		newPosition = (row,col)
		if cartCount[newPosition] > 0:
			#print(cartCount)
			print(newPosition)
			exit(0)
		cartCount[newPosition] += 1

		if field[newPosition] == "+":
			if turnCount[cid]%3 == 0:
				#print(cid, "left")
				nd = turnLeft(dire)
			elif turnCount[cid]%3 == 1:
				#print(cid, "straight")
				nd = dire
			elif turnCount[cid]%3 == 2:
				#print(cid, "right")
				nd = turnRight(dire)
			turnCount[cid] += 1
		elif field[newPosition] == "/":
			if dire == "<" or dire == ">":
				nd = turnLeft(dire)
			elif dire == "^" or dire == "v":
				nd = turnRight(dire)
		elif field[newPosition] == "\\":
			if dire == "<" or dire == ">":
				nd = turnRight(dire)
			elif dire == "^" or dire == "v":
				nd = turnLeft(dire)
		else:
			nd = dire

		nc.append((row,col, nd,cid))
	carts = sorted(nc)
	
