from collections import defaultdict
#input = "sample.in"
input = "input.in"
file = open(input, "r")


total = 0
for line in file:
    layer, length = map(int, line.strip().split(":"))
    
    if layer%(2*(length-1)) == 0:
        total += layer * length
print(total) 
    
    


        
        
    