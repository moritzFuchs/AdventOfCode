#input = "sample2.in"
input = "input.in"

def doIt(line):
    l = sorted(list(map(int, line.split())))
    for ind in range(0,len(l)):
        for ind2 in range(ind+1, len(l)):
            if l[ind2] % l[ind] == 0:
                return l[ind2] // l[ind] 

file = open(input, "r")

total = 0
for line in file:
    total += doIt(line)
    
    
print(total)