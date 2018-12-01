#input = "sample.in"
input = "input.in"

file = open(input, "r")

total = 0
for line in file:
    ma, mi = 0,1000000000000000000000000000
    for x in map(int, line.split()):
        if x > ma: ma = x
        if x < mi: mi = x
    total += ma-mi
print(total)
        
    