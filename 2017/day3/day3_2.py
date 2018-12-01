from math import sqrt 
from collections import defaultdict
#input = "sample2.in"
input = "325489"
x = int(input)

def sumUp(d, pos):
    total = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 or j != 0:
                total += d[(pos[0]+i, pos[1]+j)]
    return total
    

def doIt():
    d = defaultdict(int)
    pos = (0,0)
    
    d[pos] = 1
    
    inc = 1
    dir = 1
    while True:
        for _ in range(inc):
            pos = (pos[0]+dir,pos[1])
            n = sumUp(d,pos)
            print(pos, n)
            d[pos] = n
            if d[pos] > x:
                return d[pos] 
            
        for _ in range(inc):
            pos = (pos[0],pos[1]+dir)
            n = sumUp(d,pos)
            print(pos, n)
            d[pos] = n
            if d[pos] > x:
                return d[pos]
            
        dir *= -1
        inc += 1

print(doIt())