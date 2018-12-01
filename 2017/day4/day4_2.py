#input = "sample2.in"
input = "input.in"

file = open(input, "r")

total = 0
for line in file:
    seen = set()
    add = 1
    for x in line.strip().split(" "):
        tmp = "".join(sorted(x))
        if tmp in seen:
            add = 0
            break
        seen.add(tmp)
    total += add

print(total)