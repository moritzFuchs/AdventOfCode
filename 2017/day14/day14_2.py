from functools import reduce
#input = "sample.in"
input = "sample.in"

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
    
total = 0
grid = []
for i in range(128):
    currentPosition = 0
    skipSize = 0
    line = "stpzcrnm-" + str(i)
    
    lengths = [ord(x) for x in line.strip()] + salt
    
    result = [x for x in range(resultSize)]
    for i in range(64):
        result = hashRound(lengths, result)
    
    dh = []
    output = ""
    for i in range(16):
        tmp = reduce(lambda x,y: x^y, result[16*i:16*(i+1)])
        dh.append(format(tmp, '08b'))
        
    grid.append([1 if x == "1" else 0 for x in "".join(dh)])
    total += "".join(dh).count("1")

directions = [(1,0),(0,1),(-1,0),(0,-1)]
seen = set()
total = 0
for i in range(128):
    for j in range(128):
        if grid[i][j] == 1:
            total += 1
            q = [(i,j)]
            grid[i][j] = 0
            while q:
                a,b = q.pop(0)
                print(a,b)
                
                for x,y in directions:
                    if a+x >= 0 and a+x < 128 and b+y >= 0 and b+y < 128 and grid[a+x][b+y] == 1:
                        q.append((a+x, b+y))
                        grid[a+x][b+y] = 0
            
                        
                
for x in grid:
    print(x)   

print(total)
    
