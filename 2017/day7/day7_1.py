from collections import defaultdict 

#input = "sample.in"
input = "input.in"

file = open(input, "r")

indeg = defaultdict(int)
all = set()
for line in file:
    split = line.split("->")
    
    x = split[0].split()[0].strip()
    all.add(x)
    if len(split) > 1:
        for x in split[1].split(","):
            indeg[x.strip()] += 1
        

for x in all:
    if indeg[x] == 0:
        print(x)