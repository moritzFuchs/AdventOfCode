input = "input.in"
file = open(input, "r")

x = 0
for line in file:
    x += int(line)
print(x) 

