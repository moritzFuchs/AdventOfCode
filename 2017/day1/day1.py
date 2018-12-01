x = input()
total = 0
for ind in range(0, len(x)):
    if x[ind] == x[(ind+len(x)//2)%len(x)]:
        total += int(x[ind])

print(total)        
    