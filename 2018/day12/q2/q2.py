from collections import defaultdict

def score(state,l):
	res = 0
	for i in range(-l,l+1):
		if state[i+l] == "#":
			res += i-1
	return res

input = "input.in"
file = open(input, "r")
state = ""

l = 40000
state = ["." for _ in range(2*l+1)]
a = [x for x in file.readline()[15:].strip()]
state[l+1:l+1+len(a)] = a

file.readline()
m = defaultdict(lambda:".")
for line in file:
	m[line[:5]] = line[9]

scores = [(score(state,l),0)]
it = 500
for x in range(it):
	#print("".join(state))
	ns = [x for x in state]
	for i in range(2,len(state)-2):
		ns[i] = m["".join(state[i-2:i+3])]
	state = ns
	s = score(state,l)
	p = scores[-1][0]
	scores.append((s, s-p,x))

print(scores)
print(score(state,l))

print(scores[-1][0] + (scores[-1][1] * (50000000000-it)))