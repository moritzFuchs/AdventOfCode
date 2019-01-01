input = 320851

state = [3,7]
p1,p2 = 0,1

while len(state) < input + 10:
	for z in str(state[p1] + state[p2]):
		state.append(int(z))
	p1 = (p1+1+state[p1])%len(state)
	p2 = (p2+1+state[p2])%len(state)
	
print("".join(str(x) for x in state[input:input+10]))