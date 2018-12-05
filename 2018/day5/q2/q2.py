import string

input = "input.in"
file = open(input, "r")

for line in file:
	mi = 10000000000000000
	for c in string.ascii_lowercase:
		l = line.replace(c,"")
		l = l.replace(c.upper(),"")
		
		found = True
		while found:
			found = False
			for c in string.ascii_lowercase:
				size = len(l)
				l = l.replace("%s%s"%(c,c.upper()), "")
				l = l.replace("%s%s"%(c.upper(),c), "")
				if size != len(l):
					found = True
		mi = min(len(l),mi)
		
	print(mi)
