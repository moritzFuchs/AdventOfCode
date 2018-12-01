from collections import defaultdict 
#input = "sample.in"
input = "input.in"

file = open(input, "r")

for line in file:
    
    total = 0
    totalRemoved = 0
    
    skip = False
    depth = 0
    garbage = False
    
    for i in range(len(line)):
        if skip:
            skip = False
            continue
        
        if garbage:
            if line[i] == "!":
                skip = True
                continue
            if line[i] == ">":
                garbage = False
                continue
            
            totalRemoved += 1
        else:
            
            if line[i] == "!":
                skip = True
            
            if line[i] == "{":
                depth += 1
            
            if line[i] == "}":
                total += depth
                depth -= 1
            if line[i] == "<":
                garbage = True
    print(total, totalRemoved)
    