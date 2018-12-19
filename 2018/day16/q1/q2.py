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

input = "input2.in"
file = open(input, "r")

m = {1: 'borr', 2: 'addi', 12: 'mulr', 4: 'addr', 0: 'bori', 3: 'muli', 9: 'seti', 13: 'eqri', 8: 'gtrr', 10: 'eqir', 6: 'gtri', 11: 'eqrr', 14: 'gtir', 7: 'setr', 15: 'banr', 5: 'bani'}
state = [0,0,0,0]

for line in file:
	instr = list(map(int, line.split()))
	if m[instr[0]] == "addr":
		addr(state, instr)
	elif m[instr[0]] == "addi":
		addi(state, instr)
	elif m[instr[0]] == "mulr":
		mulr(state, instr)
	elif m[instr[0]] == "muli":
		muli(state, instr)
	elif m[instr[0]] == "banr":
		banr(state, instr)
	elif m[instr[0]] == "bani":
		bani(state, instr)
	elif m[instr[0]] == "borr":
		borr(state, instr)
	elif m[instr[0]] == "bori":
		bori(state, instr)
	elif m[instr[0]] == "setr":
		setr(state, instr)
	elif m[instr[0]] == "seti":
		seti(state, instr)
	elif m[instr[0]] == "gtir":
		gtir(state, instr)
	elif m[instr[0]] == "gtri":
		gtri(state, instr)
	elif m[instr[0]] == "gtrr":
		gtrr(state, instr)
	elif m[instr[0]] == "eqir":
		eqir(state, instr)
	elif m[instr[0]] == "eqri":
		eqri(state, instr)
	elif m[instr[0]] == "eqrr":
		eqrr(state, instr)

print(state[0])
