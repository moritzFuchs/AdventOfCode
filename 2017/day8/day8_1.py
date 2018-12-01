from collections import defaultdict 

def conditionMet(d, variable, cond, amount):
    if cond == ">":
        return d[variable] > amount
    if cond == "<":
        return d[variable] < amount
    if cond == ">=":
        return d[variable] >= amount
    if cond == "<=":
        return d[variable] <= amount
    if cond == "==":
        return d[variable] == amount
    if cond == "!=":
        return d[variable] != amount


#input = "sample.in"
input = "input.in"

file = open(input, "r")
values = defaultdict(int)
ma = 0
for line in file:
    split = line.strip().split(" ")
    variable = split[0]
    operation = split[1]
    amount = int(split[2])
    
    condVariable = split[4]
    cond = split[5]
    condAmount = int(split[6])
    
    if conditionMet(values, condVariable, cond, condAmount):
        if operation == "inc":
            values[variable] += amount
        else:
            values[variable] -= amount
        ma = max(ma, values[variable])

print(ma)
        