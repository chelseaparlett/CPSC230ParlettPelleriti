# FOR LOOPS
dennis = '''Listen, strange women lyin
 in ponds distributin swords is no basis
  for a system of government! Supreme
   executive power derives from a mandate
    from the masses, not from some farcical
     aquatic ceremony!'''

for item in dennis:
    if item in "dennis":
        print(item, "!")
#-------------------------------------------
d = 0
for let in dennis:
    if let == 'd':
        d += 1
print(d)
#-------------------------------------------
s = 0
for let in dennis:
    if let in "sS":
        s += 1
print(s)
#-------------------------------------------

for i in range(0,10):
    print(i)

#rewrite as for LOOPS
#-------------------------------------------
f ==  0

 while  f < 25:
    if f%2 == 0:
        f += 1
        continue
    else:
        f += 1
        print("odd")
