from collections import defaultdict
input = "sample.in"
#input = "input.in"
file = open(input, "r")

def find(x):
    if parent[x] == x:
        return x
    res = find(parent[x])
    parent[x] = res
    return res

def union(x,y):
    xa = find(x)
    xb = find(y)
    if xa != xb:
        parent[xa] = xb
        size[xb] += size[xa]


parent = dict()
size = dict()

for line in file:
    sp = line.strip().split("<->")
    
    start = int(sp[0].strip())
    if start not in parent:
        parent[start] = start
        size[start] = 1
    for end in sp[1].strip().split(","):
        end = int(end.strip())
        if end not in parent:
            parent[end] = end
            size[end] = 1
        union(start, end)

seen = set()
for x in parent.keys():
    seen.add(find(x))

print(seen)
print(len(seen))


        
        
    