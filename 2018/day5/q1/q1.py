import string

input = "input.in"
file = open(input, "r")

for line in file:
	found = True
	while found:
		found = False
		for c in string.ascii_lowercase:
			size = len(line)
			line = line.replace("%s%s"%(c,c.upper()), "")
			line = line.replace("%s%s"%(c.upper(),c), "")
			if size != len(line):
				found = True
	
	print(len(line))
