from collections import defaultdict

input = "input.in"
file = open(input, "r")
state = ""

l = 400
state = ["." for _ in range(2*l+1)]
a = [x for x in file.readline()[15:].strip()]
state[l+1:l+1+len(a)] = a

file.readline()
m = defaultdict(lambda:".")
for line in file:
	m[line[:5]] = line[9]

for _ in range(20):
	print("".join(state))
	ns = [x for x in state]
	for i in range(2,len(state)-2):
		ns[i] = m["".join(state[i-2:i+3])]
	state = ns

res = 0
for i in range(-l,l+1):
	if state[i+l] == "#":
		print(i-1)
		res += i-1
print(res)