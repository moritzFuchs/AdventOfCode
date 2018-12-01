from collections import defaultdict
#input = "sample.in"
input = "input.in"
file = open(input, "r")


total = 0
seclayers = dict()
for line in file:
    layer, length = map(int, line.strip().split(":"))
    seclayers[layer] = length


done = False
total = 0
offset = 0
while not done:
    done = True
    offset += 1
    for layer,length in seclayers.items():
        if (layer + offset)%(2*(length-1)) == 0:
            done = False
            break
    
        
print(offset)    
    
    


        
        
    