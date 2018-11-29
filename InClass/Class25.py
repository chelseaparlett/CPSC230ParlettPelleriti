# list comp

a= [[1,2,3,4,42,4,3,2],[4,2,3,9,5,83,8,2,9,0,3], [4,8,15,16,23,42]]

b = []
for sub in a:
    for i in sub:
        b.append(str(i+1))
print(b)
#make a list with all the values from these 3 lists using list comprehension

b2 = [str(i+1) for sub in a for i in sub]
print(b2)


b = [10,67,89,7,4,90,127,1024]
c = [x*10 for x in b if x>10]

print(c)

for x in b:
    if x > 10:
        c.append(x*10)
