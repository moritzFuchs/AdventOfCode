from collections import defaultdict
input = "input.in"
file = open(input, "r")

ids = []

for line in file:
	ids.append(line.strip())

for i in range(len(ids)):
	for j in range(i+1, len(ids)):
		res = []
		for idx in range(len(ids[i])):
			if ids[i][idx] == ids[j][idx]:
				res.append(ids[j][idx])
		
		if len(res) == len(ids[i])-1:
			print("".join(res))
			exit(0);
