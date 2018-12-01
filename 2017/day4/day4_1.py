#input = "sample.in"
input = "input.in"

file = open(input, "r")

total = 0
for line in file:
    seen = set()
    add = 1
    for x in line.strip().split(" "):
        if x in seen:
            add = 0
            break
        seen.add(x)
    total += add

print(total)