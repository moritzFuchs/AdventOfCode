input = "input.in"
file = open(input, "r")

freqChange = []
for line in file:
    freqChange.append(int(line))

seen = set()

x = 0
idx = 0
while (x not in seen):
    seen.add(x)
    x += freqChange[idx]
    idx += 1
    idx %= len(freqChange)

print(x) 

