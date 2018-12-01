from math import sqrt 

#input = "sample2.in"
input = "325489"

x = int(input)-1
n2 = int(1/2 * (-1+sqrt(1+4*x)))

tmp = (n2+1)//2
if n2%2 == 0:
    pos = (-tmp,-tmp)
    direction = 1
else:
    pos = (tmp,tmp)
    direction = -1
     
current_add = n2+1
current = n2**2 + n2

if x - current >= current_add:
    pos = (pos[0]+(direction * current_add), pos[1])
    current += current_add
    pos = (pos[0], pos[1] + direction*(x - current))
else:
    pos = (pos[0]+direction*(x-current), pos[1])
 

print(abs(pos[0]) + abs(pos[1]))