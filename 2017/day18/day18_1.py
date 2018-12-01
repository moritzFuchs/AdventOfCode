from collections import defaultdict
#input = "sample.in"
input = "input.in"


file = open(input, "r")

def getValue(regOrValue):
    if regOrValue in register:
        return register[regOrValue]
    return int(regOrValue)

register = defaultdict(int)
sound = -1
operations = []

for line in file:
    operations.append(line)

pos = 0
res = -1
while pos >= 0 and pos < len(operations):
    sp = operations[pos].strip().split()
    
    #print(pos)
    if sp[0] == "set":
        reg = sp[1]
        num = getValue(sp[2])
        register[reg] = num
    
    if sp[0] == "add":
        register[sp[1]] += getValue(sp[2])
    
    if sp[0] == "mul":
        register[sp[1]] *= getValue(sp[2])
    if sp[0] == "mod":
        register[sp[1]] %= getValue(sp[2])
    if sp[0] == "snd":
        sound = getValue(sp[1])
    if sp[0] == "rcv":
        if getValue(sp[1]) != 0:
            register[sp[1]] = sound
        if res == -1:
            res = sound
            break
    if sp[0] == "jgz":
        if getValue(sp[1]) > 0:
            pos += getValue(sp[2])
            continue
    
    pos += 1



print(res)