
#skip = 3
skip = 382


length = 1
zeropos = 0
pos = 0
res = -1
for i in range(1,50000001):
    pos = (pos + skip)%length
    if pos == zeropos:
        res = i
    
    if pos < zeropos:
        zeropos += 1
    
    pos = pos + 1
    length += 1

print(res)
    