from collections import defaultdict
import re

# Horrible code incoming..

IMMUNE_SYSTEM = 0
INFECTION = 1

class Group:
	num = 0
	hitpoints = 0
	immuneTo = []
	weakTo = []
	damage = 0
	damageType = ""
	initiative = 0
	army = 0
	id = 0

	attacked = False
	attacks = None
	dead = False

	def takeDamage(self, other):
		damage = self.damageFrom(other)
		if damage == 0:
			return
		self.num -= damage // self.hitpoints
		if self.num <= 0:
			self.dead = True

	def canAttack(self, other):
		return (not other.attacked) and self.army != other.army

	def effectivePower(self):
		return self.num * self.damage;

	def damageFrom(self, other):
		if other.damageType in self.immuneTo:
			return 0
		damage = other.effectivePower()
		if other.damageType in self.weakTo:
			damage *= 2
		return damage

	def __str__(self):
		ret = ""
		ret += "Id: {}\n".format(self.id)
		ret += "Effective Power: {}\n".format(self.effectivePower())
		ret += "Number of units: {}\n".format(self.num)
		ret += "Immune to: {}\n".format(self.immuneTo)
		ret += "Weak to: {}\n".format(self.weakTo)
		ret += "Damage: {}\n".format(self.damage)
		ret += "Damage type: {}\n".format(self.damageType)
		ret += "Initiative: {}\n".format(self.initiative)
		#ret += "Attacks: {}\n".format(self.attacks.effectivePower())
		ret += "Is attacked: {}\n".format(self.attacked)
		return ret

	def __lt__(self, other):
		if self.effectivePower() == other.effectivePower():
			return self.initiative > other.initiative
		return self.effectivePower() > other.effectivePower()

input = "input.in"
file = open(input, "r")

regex = r"(\d+)[a-z\s]*(\d+)[a-z\s]*((?:\((?:[a-z\s;,]*)\))?)[a-z\s]*(\d+)\s([a-z]*)\s[a-z\s]*(\d+)"

groups = []
t = IMMUNE_SYSTEM
i=1
for line in file:
	if line.strip() == "Immune System:":
		continue
	elif line.strip() == "Infection:":
		t = INFECTION
		i = 1
		continue

	matches = re.finditer(regex, line)
	m = re.match(regex, line)
	
	g  = Group()

	g.num = int(m.group(1))
	g.hitpoints = int(m.group(2))
	strengthWeakness = m.group(3)[1:-1]
	g.damage = int(m.group(4))
	g.damageType = m.group(5)
	g.initiative = int(m.group(6))
	g.army = t
	g.id = (t,i)
	i += 1

	if strengthWeakness != "":
		sp = strengthWeakness.split(";")
		if sp[0].split(" ")[0] == "immune":
			g.immuneTo = [x.replace(",","").strip() for x in sp[0].strip().split(" ")[2:]]
			if len(sp) == 2:
				g.weakTo = [x.replace(",","").strip() for x in sp[1].strip().split(" ")[2:]]
		else:
			g.weakTo = [x.replace(",","").strip() for x in sp[0].strip().split(" ")[2:]]

	groups.append(g)
while True:
	attacks = []
	for x in sorted(groups, key=lambda x:(-x.effectivePower(), -x.initiative)):
		maxDamage = 0
		maxDamageGroups = []

		for g in groups:
			if x.canAttack(g):
				damage = g.damageFrom(x)
				if damage > maxDamage:
					maxDamage = damage
					maxDamageGroups = [g]
				elif damage == maxDamage:
					maxDamageGroups.append(g)
		
		if maxDamage > 0 and len(maxDamageGroups) > 0:
			g = sorted(maxDamageGroups, key=lambda x: (-x.effectivePower(), -x.initiative))[0]
			x.attacks = g
			g.attacked = True
			attacks.append((x,g))
		
	for g in sorted(groups, key=lambda x: x.initiative, reverse=True):
		if not g.dead and g.attacks != None:
			g.attacks.takeDamage(g)
	ng = []
	total = [0,0]
	for g in groups:
		if not g.dead:
			g.attacks = None
			g.attacked = False
			ng.append(g)
			total[g.army] += 1
	groups = ng
	if total[0] == 0 or total[1] == 0:
		break
	
print(sum([x.num for x in groups]))