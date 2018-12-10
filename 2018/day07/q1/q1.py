import string
from collections import defaultdict
import heapq

input = "input.in"
file = open(input, "r")

inDeg = defaultdict(int)
adj = defaultdict(lambda:[])

q = []
heapq.heapify(q)
n = set()

for line in file:
	sp = line.split()
	start, end  = sp[1], sp[7]
	n.add(start)
	n.add(end)
	adj[start].append(end)
	inDeg[end] += 1
	
for x in n :
	if inDeg[x] == 0:
		heapq.heappush(q,x)
res = ""

while q:
	x = heapq.heappop(q)
	res += x
	for a in adj[x]:
		inDeg[a] -= 1
		if inDeg[a] == 0:
			heapq.heappush(q,a)
print(res)



