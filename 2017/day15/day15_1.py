
#input = "sample.in"
input = "sample.in"


file = open(input, "r")
 
A = 679
B = 771

genAFactor = 16807
genBFactor = 48271
mod = 2147483647

mask = 2**16-1

total = 0
for _ in range(40000000):
    A = (A * genAFactor) % mod
    B = (B * genBFactor) % mod
    
    tA = A & mask
    tB = B & mask
    
    if tA == tB:
        total += 1 
    
print(total)