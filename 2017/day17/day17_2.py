
#skip = 3
skip = 382

l = [0]
pos = 0
res = -1
for i in range(1,50000001):
    pos = (pos + skip)%len(l)
    if l[pos] == 0:
        res = i
    l = l[:pos+1] + [i] + l[pos+1:]
    pos = pos + 1

print(res)
    