from collections import defaultdict
import re

def distance(bot1, bot2):
	res = 0
	for i in range(3):
		res += abs(bot1[i] - bot2[i])
	return res

input = "input.in"
file = open(input, "r")

regex = r"pos=<([-]?\d+),([-]?\d+),([-]?\d+)>,\sr=(\d+)"

bots = []
maxRadBot = (0,0,0,0)

for line in file:
	matches = re.finditer(regex, line)
	m = re.match(regex, line)
	x = int(m.group(1))
	y = int(m.group(2))
	z = int(m.group(3))
	r = int(m.group(4))
	nb = (x,y,z,r)

	bots.append(nb)

	if r > maxRadBot[3]:
		maxRadBot = nb

total = 0
for bot in bots:
	if distance(bot, maxRadBot) <= maxRadBot[3]:
		total += 1
print(total)