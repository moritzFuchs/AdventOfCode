#input = "sample.in"
input = "input.in"

file = open(input, "r")

jumplist = []
for line in file:
    jumplist.append(int(line.strip()))


current = 0
total = 0
while current < len(jumplist) and current >= 0:
    next = current + jumplist[current]
    if jumplist[current] >= 3:
        jumplist[current] -= 1
    else:
        jumplist[current] += 1
    current = next
    total += 1
print(total)
