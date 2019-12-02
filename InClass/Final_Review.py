#classes------------------------------------------------------
class wizard:
    def __init__(self,name,specialpower):
        self.myclass = "wizard"
        self.name = name
        self.sp = specialpower
        self.hp = 100
        print("---------------------------------------------")
        print("Welcome " + self.name + " to the Battle Game.")
        print("You are a " + self.myclass)
        print("You have " + str(self.hp) + " health.")
        print("---------------------------------------------")

    def basic_attack(self, attackee):
        damage = random.randint(0,6)
        attackee.hp -= damage
        print("---------------------------------------------")
        print(self.name + " did " + str(damage) +\
         " damage to " + attackee.name)
        print(attackee.name + "'s health is now at " + str(attackee.hp))
        print("---------------------------------------------")
        return(attackee)

import random
harry = wizard("Harry", {"name": "patronus", "damage": [10,20], "cooldown": 2})
ron = wizard("Ron", {"name": "accio", "damage": [5,50], "cooldown": 3})

harry.basic_attack(ron)
ron.basic_attack(harry)

#functions------------------------------------------------------
import random

#How many rolls will it take me on average to roll a 1?
def rolltillone():
    roll = 0
    count = 0
    rolls = []
    while roll != 1:
        roll = random.randint(1,6)
        count += 1
        rolls.append(roll)
    #print(rolls)
    return(count)

# l = rolltillone()
# print(l)

n = 10000
simulation = [rolltillone() for i in range(0,n)]
#print(simulation)
print(sum(simulation)/n)

#what about a 20 sided die?

def multChoiceGrader(correct = ["A","B","C","A","C","B","A","A","D"], answers):
    if len(correct) != len(answres):
        print("There's a problem here")
        return(0)

    correctAns = 0
    for i in len(correct):
        if correct[i] == answers[i]:
            correctAns += 1
    return(correctAns/len(correct)) #percentage correct

#files----------------------------------------------------------
def andCounter(filename):
    f = open(filename, "r")
    ac = 0
    i = 0
    for line in f:
        i += 1
        for word in line.split(" "):
            if word.lower() == "and":
                ac += 1
                print("and found on line " + str(i)) #what if I wrote this to a file instead?
andCounter("Song.txt")
#list comprehension---------------------------------------------
cards = ["A","K","Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
suits = ["diamonds", "clubs", "spades", "hearts"]

deck = [(card + " " suit) for suit in suits for card in cards]

#---
def palindrome(word = "racecar"):
    word = word.lower()
    word = word.replace(" ","")replace(".","").replace(",","").replace("!","")
    return(word == word[::-1])

# w = []
# for word in words:
#     if palindrome(word):
#         w.append(word)

words = ["ballon", "kayak", "Mr Owl Ate My Metal Worm", "apple", "A Santa Lived As a Devil At NASA"]

w = [word for word in words if palindrome(word)]
print(w)

#---

message = input("Type Message Here: ")
message = message.split()
bad = ["crap", "dang", "fudge"]

# for word in message:
#     if word not in bad:
#         k.append(word)
#     else:
#         k.append("*"*len(word))

k = [word if word not in bad else "*"*len(word) for word in message]
print(" ".join(k))

#SpongeMock
m = "Antidisestablishmentarianism"

sponge = [m[i].lower() if i%2 else m[i].upper() for i in range(0,len(m))]
print("".join(sponge))
#---
