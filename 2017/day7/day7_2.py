from collections import defaultdict

#input = "sample.in"
input = "input.in"

file = open(input, "r")

weight = dict()
out = dict()

indeg = defaultdict(int)
all = set()
for line in file:
    split = line.split("->")

    x = split[0].split()[0].strip()
    all.add(x)
    w = int(split[0].split()[1].strip()[1:-1])
    weight[x] = w
    out[x] = list()
    
    if len(split) > 1:
        for n in split[1].split(","):
            out[x].append(n.strip())
            indeg[n.strip()] += 1

root = -1
for x in all:
    if indeg[x] == 0:
        root = x

totalWeight = dict()

def getWeight(x):
    if x in totalWeight:
        return totalWeight[x]
    
    totalWeight[x] = weight[x]
    for a in out[x]:
        totalWeight[x] += getWeight(a)
    return totalWeight[x]

def fix(l):
    d = defaultdict(list)
    diffWeights = set()
    for x in l:
        w = getWeight(x)
        print(x + ": " + str(w))
        diffWeights.add(w)
        d[w].append(x)
    
    if len(diffWeights) > 1:
        
        for x in l:
            if len(out[x]) > 0:
                ret = fix(out[x])
                if ret != -1:
                    return ret
        
        
        for a in diffWeights:
            if len(d[a]) == 1:
                toFix = d[a][0]
                currentTotalWeight = a
                break
        
        targetWeight = -1
        for a in diffWeights:
            if a != currentTotalWeight:
                targetWeight = a
                break
        
        print(toFix, targetWeight, currentTotalWeight, diffWeights)
        
        weightDiff = targetWeight - currentTotalWeight
        newWeight = weight[toFix] + weightDiff
        return newWeight
        
    else:
        for x in l:
            if len(out[x]) > 0:
                ret = fix(out[x])
                if ret != -1:
                    return ret
                
    return -1
    

print(fix(out[root]))
    