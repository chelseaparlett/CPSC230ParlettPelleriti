#DICTIONARY REVIEW

hp = {
    "harry": {"house": "Gryffindor", "patronus": "Stag"},
    "hermione": {"house":"Gryffindor", "patronus": "Otter" },
    "luna": {"house":"Ravenclaw", "patronus": "Hare" },
    "snape": {"house":"Slytherin", "patronus": "Doe" },
    "ron": {"house":"Gryffindor", "patronus": "Jack Russell Terrier" }
}

# CAN I get the first item out of the dictionary?
# Do dictionaries have indicies?
hp["harry"]
# A New Student is enrolling. How do I add them?
hp["ginny"]= {"house": "Gryffindor", "patronus": "Horse"}

name = input("Which character do you want? ")

patronus = hp[name]["patronus"]

# how can I loop through the keys of a dictionary?

for n in hp.values():

d = {}
a = [["1",2], ["2",6]]
a[0][0]
for i in a:
    d[i[0]] = i[1]

print(d)
print(d["1"])
d.keys()
