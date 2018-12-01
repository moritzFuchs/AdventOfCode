from collections import defaultdict
#input = "sample.in"
input = "input.in"

resultSize = 256
file = open(input, "r")

moves_map = {
    ("n","s"): (),
    ("nw","ne"): ("n",),
    ("sw","se"): ("s",),
    ("n","sw"): ("nw",),
    ("n","se"): ("ne",),
    ("s","nw"): ("sw",),
    ("s","ne"): ("se",),
    
    }

counts = defaultdict(int)

for line in file:
    current = (0,0)
    ma = 0
    
    split = line.strip().split(",")
    for x in split:
        
        counts[x] += 1
        change = True
        while change:
            change = False
        
            for start, end in moves_map.items():
                print(start, end)
                if counts[start[0]] > 0 and counts[start[1]] > 0:
                    counts[start[0]] -= 1
                    counts[start[1]] -= 1
                    for x in end:
                        counts[x] += 1
                    change= True
        
        ma = max(ma, sum(counts.values()))
        
    print(counts)
    print(sum(counts.values()))
    print(ma)
        
    