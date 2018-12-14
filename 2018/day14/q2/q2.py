input = "320851"

state = [3,7]
p1,p2 = 0,1

pos = 0
num = 2

while True:
	for z in str(state[p1] + state[p2]):
		x = int(z)
		state.append(x)
		num += 1
		if z == input[pos]:
			pos += 1
			if pos == len(input):
				print(num - pos)
				exit(0)
		else:
			# no suffix of our input is a prefix of the input
			pos = 0
			if z == input[0]:
				pos = 1

	p1 += 1+state[p1]
	p1 %= len(state)

	p2 += 1+state[p2]
	p2 %= len(state)

