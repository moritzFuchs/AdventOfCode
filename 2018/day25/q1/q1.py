import collections

class MyDD(collections.defaultdict):
    def __missing__(self, key):
        self[key] = value = key
        return value

def find(item):
	if uf[item] == item:
		return item
	res = find(uf[item])
	uf[item] = res
	return res

def union(item1, item2):
	x1 = find(item1)
	x2 = find(item2)

	uf[x1] = x2

def distance(p1, p2):
	res = 0
	for i in range(4):
		res += abs(p1[i] - p2[i])
	return res

input = "sample3.in" # 2
input = "sample2.in" # 8
input = "sample1.in" # 3
input = "sample.in" # 4
input = "input.in" # ?
file = open(input, "r")

uf = MyDD()

points = []
for line in file:
	p = tuple(map(int, line.split(",")))
	for p2 in points:
		if distance(p,p2) <= 3:
			union(p,p2)
	points.append(p)

total = set()
for p in points:
	total.add(find(p))
print(len(total))
