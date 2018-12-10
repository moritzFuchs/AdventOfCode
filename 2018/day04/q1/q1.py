from collections import defaultdict
from datetime import datetime
import operator
import re 

input = "input.in"
file = open(input, "r")
regex = r"Guard\s#(\d+)\sbegins\sshift"

log = []


for line in file:
	line = line.strip()
	# [1518-11-01 00:00] Guard #10 begins shift
	date = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
	message = line[19:]
	if message.startswith("Guard"):
		matches = re.finditer(regex, line)
		m = re.match(regex, message)
		idx = int(m.group(1))
		log.append((date, idx))
	elif message == "falls asleep":
		log.append((date, -1))
	elif message == "wakes up":
		log.append((date, -2))
	else:
		print(message)
log.sort()

sleepCount = defaultdict(int)
sleepStat = defaultdict(lambda: [0]*60)

currentIdx = -1
maxSleep = 0
maxSleepIdx = -1
for i in range(len(log)):
	if log[i][1] >= 0:
		currentIdx = log[i][1]
	elif log[i][1] == -1:
		start = log[i][0].minute
		end = log[i+1][0].minute
		diff = end-start
		for j in range(start, end):
			sleepStat[currentIdx][j] += 1
		sleepCount[currentIdx] += diff
		if sleepCount[currentIdx] > maxSleep:
			maxSleep = sleepCount[currentIdx]
			maxSleepIdx = currentIdx



ma = -1
maidx = -1

for i in range(59):
	if sleepStat[maxSleepIdx][i] > ma:
		maidx = i
		ma = sleepStat[maxSleepIdx][i]

print(maidx, maxSleepIdx, maidx * maxSleepIdx)
