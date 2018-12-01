from collections import defaultdict
#input = "sample.in"
input = "input.in"
#input = "sample2.in"


file = open(input, "r")

def getValue(register, regOrValue):
    if regOrValue in register:
        return register[regOrValue]
    return int(regOrValue)

operations = []
for line in file:
    operations.append(line)

registers = [defaultdict(int), defaultdict(int)]
queues = [[], []]
waiting = [False, False]
terminated = [False, False]
pos = [0,0]

registers[0]["p"] = 0
registers[1]["p"] = 1

seen = set()

res = 0
user = 0
while True:
    if pos[user] < 0 or pos[user] >= len(operations):
        terminated[user] = True
        if not terminated[(user+1)%2]:
            user = (user+1)%2
            continue
        else:
            break
 
    sp = operations[pos[user]].strip().split()
    
    s = str(user) + " " + str(pos[user]) + " " + str(registers[user])
    if s in seen:
        print(s)
    seen.add(s)
    
    if sp[0] == "set":
        reg = sp[1]
        num = getValue(registers[user], sp[2])
        registers[user][reg] = num
    
    if sp[0] == "add":
        registers[user][sp[1]] += getValue(registers[user],sp[2])
    
    if sp[0] == "mul":
        registers[user][sp[1]] *= getValue(registers[user],sp[2])
    if sp[0] == "mod":
        registers[user][sp[1]] %= getValue(registers[user],sp[2])
    if sp[0] == "snd":
        if user == 1:
            res += 1
        queues[(user+1)%2].append(getValue(registers[user],sp[1]))
        waiting[(user+1)%2] = False
    if sp[0] == "rcv":
        if len(queues[user]) == 0:
            waiting[user] = True
            user = (user+1)%2
            
            if waiting[0] and waiting[1]:
                break
        
            continue
        else:
            registers[user][sp[1]] = queues[user].pop(0)
        
    if sp[0] == "jgz":
        if getValue(registers[user], sp[1]) > 0:
            pos[user] += getValue(registers[user], sp[2])
            continue
    
    pos[user] += 1
    
    if waiting[0] and waiting[1]:
        break

print(res)