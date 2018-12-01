from collections import defaultdict 
#input = "sample.in"
input = "input.in"

resultSize = 256

file = open(input, "r")

for line in file:
    
    lengths = list(map(lambda x: int(x.strip()), line.strip().split(",")))
    
    currentPosition = 0
    skipSize = 0
    
    result = [x for x in range(resultSize)]
    
    for length in lengths:
        if currentPosition+length >= resultSize:
            
            
            tmp1 = result[currentPosition:]
            tmp2 = result[:(currentPosition+length)%resultSize]
            x = (tmp1+tmp2)[::-1]
            
            result[currentPosition:] = x[:resultSize-currentPosition]
            result[:(currentPosition+length)%resultSize] = x[resultSize-currentPosition:]
            
        else:
            result[currentPosition:(currentPosition+length)%resultSize] = result[currentPosition:(currentPosition+length)%resultSize][::-1]
            
        currentPosition = (currentPosition + length + skipSize)%resultSize
        skipSize += 1 
    
    print(result[0] * result[1])
    
