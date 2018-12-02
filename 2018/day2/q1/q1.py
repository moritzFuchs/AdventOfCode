from collections import defaultdict
input = "input.in"
file = open(input, "r")

totaltwos, totalthrees = 0,0
x = 0
for line in file:
	count = defaultdict(int)
	twos, threes = 0,0
	for ch in line:
		count[ch] += 1
		if count[ch] == 2:
			twos += 1
		elif count[ch] == 3:
			threes += 1
			twos -= 1
		elif count[ch] > 3:
			threes -= 1
	print(twos, threes)
	totaltwos += 1 if twos > 0 else 0
	totalthrees += 1 if threes > 0 else 0
print(totaltwos * totalthrees)


