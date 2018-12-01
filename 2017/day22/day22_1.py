from collections import defaultdict

def turnRight(direction):
    if direction == (-1,0): return (0,1)
    if direction == (1,0): return (0,-1)
    if direction == (0,-1): return (-1,0)
    if direction == (0,1): return (1,0)

def turnLeft(direction):
    return turnRight(turnRight(turnRight(direction)))

def invert(grid, current_position, original_infections):
    if grid[current_position] == "#":
        grid[current_position] = "."
        return 0
    else:
        grid[current_position] = "#"
        if current_position not in original_infections:
            #original_infections.add(current_position)
            return 1
        return 0

#input = "sample.in"
input = "input.in"

file = open(input, "r")

grid = defaultdict(lambda: ".")
original_infections = set()
direction = (-1,0)

row = 0
col = 0
for line in file:
    col = 0
    for c in line.strip():
        grid[(row, col)] = c
        #original_infections.add((row,col))
        col += 1
    row += 1

print(grid)

height = row
width = col

real_grid = defaultdict(lambda: ".")

current_position = (height//2, width//2)

print(current_position)

rounds = 10000
total_infections = 0
for _ in range(rounds):
    if grid[current_position] == "#":
        direction = turnRight(direction)
    else:
        direction = turnLeft(direction)
    
    total_infections += invert(grid, current_position, original_infections)
    
    current_position = (current_position[0] + direction[0], current_position[1] + direction[1])

print(total_infections)