from collections import defaultdict

def copy(input):
	return [x for x in input]

def addr(input, instruction):
	input[instruction[2]] = input[instruction[0]] + input[instruction[1]]
	return input

def addi(input, instruction):
	input[instruction[2]] = input[instruction[0]] + instruction[1]
	return input

def mulr(input, instruction):
	input[instruction[2]] = input[instruction[0]] * input[instruction[1]]
	return input

def muli(input, instruction):
	input[instruction[2]] = input[instruction[0]] * instruction[1]
	return input

def banr(input, instruction):
	input[instruction[2]] = input[instruction[0]] & input[instruction[1]]
	return input

def bani(input, instruction):
	input[instruction[2]] = input[instruction[0]] & instruction[1]
	return input

def borr(input, instruction):
	input[instruction[2]] = input[instruction[0]] | input[instruction[1]]
	return input

def bori(input, instruction):
	input[instruction[2]] = input[instruction[0]] | instruction[1]
	return input

def setr(input, instruction):
	input[instruction[2]] = input[instruction[0]]
	return input

def seti(input, instruction):
	input[instruction[2]] = instruction[0]
	return input

def gtir(input, instruction):
	input[instruction[2]] = 1 if instruction[0] > input[instruction[1]] else 0
	return input

def gtri(input, instruction):
	input[instruction[2]] = 1 if input[instruction[0]] > instruction[1] else 0
	return input

def gtrr(input, instruction):
	input[instruction[2]] = 1 if input[instruction[0]] > input[instruction[1]] else 0
	return input

def eqir(input, instruction):
	input[instruction[2]] = 1 if instruction[0] == input[instruction[1]] else 0
	return input

def eqri(input, instruction):
	input[instruction[2]] = 1 if input[instruction[0]] == instruction[1] else 0
	return input

def eqrr(input, instruction):
	input[instruction[2]] = 1 if input[instruction[0]] == input[instruction[1]] else 0
	return input

input = "input.in"
file = open(input, "r")

state = [0,0,0,0,0,0]
pointerReg = -1
pointer = 0
program = []

for line in file:
	sp = line.split()
	if line[0] == "#":
		pointerReg = int(sp[1])		
	else:
		instr = list(map(int,sp[1:]))
		program.append((locals()[sp[0]], instr))

#state = [0, 8, 10551318, 10551320, 0, 1]
#pointerReg = 1
#pointer = 9
#program = []

while pointer < len(program):
	if pointerReg != -1:
		state[pointerReg] = pointer
	#print(state)
	#if pointer == 9 and state[2] < state[3]:
		#state[2] = state[3]+1
	#	state[5] = state[3]+1
	#print(pointer, state)
	program[pointer][0](state, program[pointer][1])
	#print(pointer, program[pointer][0], program[pointer][1], state)
	if pointerReg != -1:
		pointer = state[pointerReg]
	pointer += 1

print(state[0])