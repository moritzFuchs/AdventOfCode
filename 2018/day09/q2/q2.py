from collections import deque

input = "input.in"
file = open(input, "r")

for line in file:
	sp = line.split()
	n, v = int(sp[0]), int(sp[6])*100

	score = [0] * n
	ch = deque()
	ch.append(0)
	
	for i in range(1, v+1):
		#print(i,idx, ch)
		if i%23 != 0:
			ch.rotate(-1)
			ch.append(i)
		else:
			ch.rotate(7)
			score[i%n] += i + ch.pop()
			ch.rotate(-1)
	print(max(score))
