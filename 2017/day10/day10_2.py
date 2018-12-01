from functools import reduce
#input = "sample.in"
input = "input.in"

resultSize = 256

file = open(input, "r")

currentPosition = 0
skipSize = 0

def hashRound(lengths, result):
    global currentPosition
    global skipSize
    
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
    
    return result 
    
salt = [17, 31, 73, 47, 23]
for line in file:
    
    currentPosition = 0
    skipSize = 0
    
    line = "70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41"
    
    lengths = [ord(x) for x in line.strip()] + salt
    
    result = [x for x in range(resultSize)]
    for i in range(64):
        result = hashRound(lengths, result)
    
    print(result)
    
    dh = []
    output = ""
    for i in range(16):
        tmp = reduce(lambda x,y: x^y, result[16*i:16*(i+1)])
        dh.append(format(tmp, '02x'))
        
    
    print(output, "".join(dh))
    
