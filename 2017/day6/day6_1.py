#input = "sample.in"
input = "input.in"

file = open(input, "r")

def argmax(l):
    ma = -1
    maind = -1
    for ind in range(len(l)):
        if l[ind] > ma:
            ma = l[ind]
            maind = ind
    return maind

banks = []
for line in file:
    for x in line.strip().split():
        banks.append(int(x))

seen = dict()
seen[",".join(map(lambda x: str(x), banks))] = 0 

total = 0
loops = 0
while True:
    ind = argmax(banks)
    tmp = banks[ind]
    banks[ind] = 0
    if tmp >= len(banks):
        for i in range(len(banks)):
            banks[i] += tmp // len(banks)
    tmp = tmp % len(banks)
    
    for i in range(1, len(banks)):
        if tmp == 0:
            break
        banks[(ind + i)%len(banks)] += 1
        tmp -= 1
    
    total += 1
    loops += 1
    bankstr = ",".join(map(lambda x: str(x), banks))
    
    if bankstr in seen:
        print(loops - seen[bankstr])
        break
    else:
        seen[bankstr] = loops
