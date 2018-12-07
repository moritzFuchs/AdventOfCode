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

workers = 5
penalty = 60

for line in file:
	sp = line.split()
	start, end  = sp[1], sp[7]
	n.add(start)
	n.add(end)
	adj[start].append(end)
	inDeg[end] += 1

timers = []
heapq.heapify(timers)

for x in n :
	if inDeg[x] == 0:
		heapq.heappush(q,x)

heapq.heappush(timers, 0)

doneCount = defaultdict(int)
doneTask = defaultdict(lambda: [])
doneCount[0] = workers

currentWorkers = 0
res = 0

while timers:
	time = heapq.heappop(timers)
	res = max(0,time)
	currentWorkers += doneCount[time]
	doneCount[time] = 0

	for t in doneTask[time]:
		for a in adj[t]:
			inDeg[a] -= 1
			if inDeg[a] == 0:
				heapq.heappush(q,a)
	while currentWorkers > 0:
		if len(q) > 0:
			task = heapq.heappop(q)
			finishTime = time + penalty + ord(task) - 64
			heapq.heappush(timers, finishTime)
			doneCount[finishTime] += 1
			doneTask[finishTime].append(task)
			currentWorkers -= 1
		else:
			break
	
print(res)