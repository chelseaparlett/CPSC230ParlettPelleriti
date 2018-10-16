#Harry Potter and the Python Dictionary
# We're going to write a dictonary to store spells and
# How much damage they do
spells = {}
spells["accio"] = 1
spells["avada kedavra"] = 100
spells["sectumsempre"] = 40
spells["lumos"] = 2
print(spells)

print("accio does" , spells["accio"], "damage")
print("\nI have these spells: ", list(spells.keys()), "\n\n")

#----------------------------------------
lists_in_dicts = {"primes": [2,3,5,7,11,13,17],
 "famous": ["e","pi", 0,"tau"],
  "perfect": [6,28, 496], "odd": [] }

lists_in_dicts["odd"].append(1)
lists_in_dicts["odd"].append(3)
lists_in_dicts["odd"].append(5)
lists_in_dicts["odd"].append(7)
lists_in_dicts["odd"].append(9)


print(lists_in_dicts)
#HOW can I pull  the first number out of the perfect numbers list?
p  = lists_in_dicts["perfect"][0]
print(p)
# HOW do  I get 13 from lists_in_dicts?
k = lists_in_dicts["primes"][5]
print(k)
#-----------------------------------------
hp = {
    "harry": {"house": "Gryffindor", "patronus": "Stag"},
    "hermione": {"house":"Gryffindor", "patronus": "Otter" },
    "luna": {"house":"Ravenclaw", "patronus": "Hare" },
    "snape": {"house":"Slytherin", "patronus": "Doe" },
    "ron": {"house":"Gryffindor", "patronus": "Jack Russell Terrier" }
}


#Store ron's patronus in the variable rons_patronus
rons_patronus = hp["ron"]["patronus"]

#change luna's patronus  to a Rabbit
hp["luna"]["patronus"] = "Rabbit"

hp["luna"]["hair color"] = "blonde"

print(hp)
{'snape': {'patronus': 'Doe', 'house': 'Slytherin'},
'ron': {'patronus': 'Jack Russell Terrier','house': 'Gryffindor'},
'luna': {'hair color': 'blonde','patronus': 'Rabbit', 'house': 'Ravenclaw'},
'hermione': {'patronus': 'Otter', 'house': 'Gryffindor'},
'harry': {'patronus': 'Stag', 'house': 'Gryffindor'}}
