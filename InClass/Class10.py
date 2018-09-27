#  LISTS

a = list()
b = []
print(a)
print(b)

#--------------------------------
c =  ["hello", "1", 7, [1,2], 9]
c[1]
c[-1]
c[1:3:-1]
#--------------------------------
#LISTS ARE MUTABLE!!!
a = []
print(a)
a.append("cool")
print(a)

alist = ["Couch","Core","Calm","Crisp"]
astring = "Cancelled"

alist[0] = "Camel"
astring[0] = "K"#?!?

spreadsheet = [[1,2,3,4,5],[32,5,7,8,8]]
spreadsheet[0]
spreadsheet[0].append("apple")
#--------------------------------
a = [1,2,3,4]
len(a)
#--------------------------------
a = ["cool"]
a.insert(0,"I'm")
print(a)
a.insert(1,"so")
print(a)
a.remove("I'm")
print(a)
#--------------------------------
classRoster = ["Chelsea","Chris","Julie","Adriene","Abby"]
for name in classRoster:
    print(name, ",You're doing a great job")
