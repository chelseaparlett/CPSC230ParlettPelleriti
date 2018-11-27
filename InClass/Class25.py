# list comp

a= [[1,2,3,4,42,4,3,2],[4,2,3,9,5,83,8,2,9,0,3], [4,8,15,16,23,42]]

#make a list with all the values from these 3 lists using list comprehension

new_a = [i for sub in a for i in sub]

# new_a = []
# for sub in a:
#     for i in sub:
#         new_a.append(i)

print(new_a)


b = [10,67,89,7,4,90,127,1024]
b = list(x*10 for x in b if x>10)

print(b)
