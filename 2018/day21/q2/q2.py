from collections import defaultdict

def f(a,b):
	return ((a+b) * 65899) & 0xffffff

seen = set()
last = -1
r = defaultdict(int)
while True:
	r[3] = r[5] | 65536;
	r[5] = 8586263;
	r[5] = f(r[5], r[3] & 0xff);
	r[5] = f(r[5], (r[3] >> 8) & 0xff);
	r[5] = f(r[5], (r[3] >> 16) & 0xff);
	if r[5] in seen:
		break
	last = r[5]
	seen.add(r[5])
	if r[5] == r[0]:
		break
print(last)
