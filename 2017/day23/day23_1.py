from collections import defaultdict
#input = "sample.in"
input = "input.in"
file = open(input, "r")

def getValue(regOrValue):
    if regOrValue in register:
        return register[regOrValue]
    return int(regOrValue)

register = defaultdict(int)
register['a'] = 0
register['b'] = 0
register['c'] = 0
register['d'] = 0
register['e'] = 0
register['f'] = 0
register['g'] = 0
register['h'] = 0
operations = []

for line in file:
    operations.append(line)

total = 0
pos = 0
res = -1
while pos >= 0 and pos < len(operations):
    sp = operations[pos].strip().split()

    if sp[0] == "set":
        reg = sp[1]
        num = getValue(sp[2])
        register[reg] = num
    
    if sp[0] == "sub":
        register[sp[1]] -= getValue(sp[2])
    
    if sp[0] == "mul":
        register[sp[1]] *= getValue(sp[2])
        total += 1

    if sp[0] == "jnz":
        if getValue(sp[1]) != 0:
            pos += getValue(sp[2])
            continue
    pos += 1
print(total)