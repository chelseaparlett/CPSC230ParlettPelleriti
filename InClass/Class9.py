#IMMUTABILITY

name = "Khelsea"
name[0]

name[0] = "C" #?!?

name = "Chelsea"

#ChainingMethods
string = "Super CaliF ragali sticEx peali doci ous"

print(string.upper().split(" "))

#Methods
"a".isalpha()
"10".isnumeric()
"12s".isalpha()

h = "      helllloooo        "
print(h)
print(h.strip())

"T".isupper()
"Hello".isupper()

"I'm new in town.".replace(" ", "")


csv = "Name,Age,Color\nChelsea,100,Blue,\nTony,35,Green\nHolly, 25, Pink"

rows = csv.split("\n")

for row in rows:
    print(rows.split(","))
