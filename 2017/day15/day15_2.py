

#input = "sample.in"
input = "sample.in"

file = open(input, "r")
 
seedA = 679
seedB = 771

#seedA = 65
#seedB = 8921

genAFactor = 16807
genBFactor = 48271
mod = 2147483647

mask = 2**16-1

def gen(seed, factor, div):
    current = seed
    done = 0
    while done < 5000000:
        current = (current * factor)%mod
        if current%div == 0:
            done += 1 
            yield current 

total = 0
for A,B in zip(gen(seedA,genAFactor, 4), gen(seedB,genBFactor, 8)):
    
    tA = A & mask
    tB = B & mask
    
    if tA == tB:
        total += 1 
    
print(total)