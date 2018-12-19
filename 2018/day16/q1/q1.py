from collections import defaultdict

def copy(input):
	return [x for x in input]

def addr(input, instruction):
	input[instruction[3]] = input[instruction[1]] + input[instruction[2]]
	return input

def addi(input, instruction):
	input[instruction[3]] = input[instruction[1]] + instruction[2]
	return input

def mulr(input, instruction):
	input[instruction[3]] = input[instruction[1]] * input[instruction[2]]
	return input

def muli(input, instruction):
	input[instruction[3]] = input[instruction[1]] * instruction[2]
	return input

def banr(input, instruction):
	input[instruction[3]] = input[instruction[1]] & input[instruction[2]]
	return input

def bani(input, instruction):
	input[instruction[3]] = input[instruction[1]] & instruction[2]
	return input

def borr(input, instruction):
	input[instruction[3]] = input[instruction[1]] | input[instruction[2]]
	return input

def bori(input, instruction):
	input[instruction[3]] = input[instruction[1]] | instruction[2]
	return input

def setr(input, instruction):
	input[instruction[3]] = input[instruction[1]]
	return input

def seti(input, instruction):
	input[instruction[3]] = instruction[1]
	return input

def gtir(input, instruction):
	input[instruction[3]] = 1 if instruction[1] > input[instruction[2]] else 0
	return input

def gtri(input, instruction):
	input[instruction[3]] = 1 if input[instruction[1]] > instruction[2] else 0
	return input

def gtrr(input, instruction):
	input[instruction[3]] = 1 if input[instruction[1]] > input[instruction[2]] else 0
	return input

def eqir(input, instruction):
	input[instruction[3]] = 1 if instruction[1] == input[instruction[2]] else 0
	return input

def eqri(input, instruction):
	input[instruction[3]] = 1 if input[instruction[1]] == instruction[2] else 0
	return input

def eqrr(input, instruction):
	input[instruction[3]] = 1 if input[instruction[1]] == input[instruction[2]] else 0
	return input

input = "input.in"
file = open(input, "r")

before = []
instruction = []
after = []

instrToCode = {}

total = 0
for line in file:
	line = line.strip()
	if len(before) == 0:
		before = list(map(int, line[9:-1].split(",")))
	elif len(instruction) == 0:
		instruction = list(map(int, line.split()))
	elif len(after) == 0:
		after = list(map(int, line[9:-1].split(",")))

		res = set()
		if addr(copy(before), instruction) == after:
			res.add("addr")
		if addi(copy(before), instruction) == after:
			res.add("addi")
		if mulr(copy(before), instruction) == after:
			res.add("mulr")
		if muli(copy(before), instruction) == after:
			res.add("muli")
		if bani(copy(before), instruction) == after:
			res.add("bani")
		if banr(copy(before), instruction) == after:
			res.add("banr")
		if bori(copy(before), instruction) == after:
			res.add("bori")
		if borr(copy(before), instruction) == after:
			res.add("borr")
		if setr(copy(before), instruction) == after:
			res.add("setr")
		if seti(copy(before), instruction) == after:
			res.add("seti")
		if gtir(copy(before), instruction) == after:
			res.add("gtir")
		if gtri(copy(before), instruction) == after:
			res.add("gtri")
		if gtrr(copy(before), instruction) == after:
			res.add("gtrr")
		if eqir(copy(before), instruction) == after:
			res.add("eqir")
		if eqri(copy(before), instruction) == after:
			res.add("eqri")
		if eqrr(copy(before), instruction) == after:
			res.add("eqrr")

		if instruction[0] not in instrToCode:
			instrToCode[instruction[0]] = res
		else:
			instrToCode[instruction[0]] = instrToCode[instruction[0]] & res

	else:
		before = []
		instruction = []
		after = []

q = []
for k,v in instrToCode.items():
	q.append((len(v),k,v))
q.sort()

m = {}
seen = set()

while q:
	l,k,v = q.pop(0)
	print(v, seen)
	if len(v) > 1:
		v = v - seen

	if len(v) > 1:
		print(".")
		q.append((len(v),k,v))
	else:
		m[list(v)[0]] = k
		seen.add(list(v)[0])
m2 = {}
for k,v in m.items():
	m2[v] = k
print(m2)
