
#input = "sample.in"
input = "input.in"


file = open(input, "r")

l = [x for x in "abcdefghijklmnop"]
#l = [x for x in "abcde"]

def dance(l, moves):
    for x in moves:
        if x[0] == "s":
            amount = int(x[1:])
            l = l[len(l)-amount:] + l[:len(l)-amount]
        if x[0] == "x":
            y = x[1:]
            start, end  = map(int, y.split("/"))
            l[start], l[end] = l[end], l[start]
        if x[0] == "p":
            y = x[1:]
            partner1, partner2 = y.split("/")
            for i in range(len(l)):
                if l[i] == partner1:
                    l[i] =  partner2
                    continue
                if l[i] == partner2:
                    l[i] =  partner1
                    continue
    return l

for line in file:
    sp = line.split(",")
    seen = dict()
    seen["".join(l)] = 0
    
    cycle_length = -1
    step = 1
    while True:
        l = dance(l, sp)
        l_str = "".join(l)
        print(l_str)
        if l_str in seen:
            cycle_length = step - seen[l_str]
            break
        step += 1
    
    target_moves = 10**9
    
    residual = (target_moves - (step - cycle_length)) % cycle_length
    for _ in range(residual):
        l = dance(l, sp)
    
    print("".join(l))
