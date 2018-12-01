from functools import reduce
#input = "sample.in"
input = "input.in"

resultSize = 256
file = open(input, "r")

moves = {
    "n" : (2,0),
    "s" : (-2,0),
    "ne" : (1,1),
    "nw" : (1,-1),
    "se" : (-1,1),
    "sw" : (-1,-1)
    }

for line in file:
    current = (0,0)
    
    split = line.strip().split(",")
    for x in split:
        current = (current[0] + moves[x][0], current[1] + moves[x][1])
    
    target = current
    
    print(target)
    
    current = (0,0)
    q = [(current,0)]
    seen = set()
    while q:
        current, steps = q.pop(0)
        
        if current == target:
            print(steps)
            break
        
        for x,y in moves.values():
            next = (current[0] + x, current[1] + y)
            if not next in seen:
                q.append((next, steps+1)) 
                seen.add(next)
        
    