b = 108400
c = 125400
h = 0

def isprime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

for b in range(108400, c+1, 17):
    if not isprime(b):
        h += 1

print(h)