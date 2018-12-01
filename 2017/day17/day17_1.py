
#skip = 3
skip = 382

l = [0]
pos = 0
for i in range(1,2018):
    pos = (pos + skip)%len(l)
    l = l[:pos+1] + [i] + l[pos+1:]
    pos = pos + 1

print(l[pos+1])
    