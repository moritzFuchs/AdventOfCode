
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
    l = dance(l, sp)
    
    print("".join(l))
