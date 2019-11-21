# Types ---------------------------------------

## ---Lists------------------------------------
a = [1,2,3, "apple", [1,2,3]]

b = "hello"
b = list(b)
print(b)

c = []

for i in "THIS IS MY LAST RESORT":
    c.append(i)

d = ["This", "is", "bull", "crap"]
d.remove("crap")
print(d)

e = [1,2,3,4,5,6,7,8]
f = 0
for x in e:
    f += x
print(f)

print(sum(e))

print(e*2)
## ---Dictionaries-----------------------------
g = {}
g = dict()

g["Name"] = "Helen"
print(g)
g["Name"] = "Grant"
print(g)

hp = {"harry": {"house": "Gryffindor", "age": 12},
"hermione": {"house": "Gryffindor", "age": 12},
"draco": {"house": "Slytherin", "age": 12}}

# add 1 to harry's age
hp["harry"]["age"] += 1

# use a loop to add 1 to everyone's age

for p in hp:
    hp[p]["age"] += 1
print(hp)


## ---Sets-------------------------------------
h = {1,2,3,4,5,6,6,7,8,9}
print(h)

i = ["this", "land", "is", "my", "land", "this", "land", "is", "your", "land"]
uniqueWords = set(i)
print(uniqueWords)

## ---Tuples-----------------------------------

j = (1,2,3)
j[0] = 0

## ---Strings----------------------------------
k = "In terms of instant relief, canceling plans is like heroin"

k2 = k.replace("e", "3")
print(k2)

print(k.upper())
print(k.isalpha())

count = 0
for i in k:
    if i == "l":
        count += 1
print(count)

k3 = k + k
l = "Na" * 8
print(l + " Batman!")

## ---Int and Float----------------------------
l = 29.2
print(int(l))

# For-------------------------------------------
dict2 = {"hello": 10, "goodbye": 13, "aloha": 23}
list2 = [1,2,3,4,5,6,7]
string2 = "Sir This is a Wendys"

for i in dict2:
    print(i)
for i in list2:
    print(i)
for i in string2:
    print(i)

# While-----------------------------------------
def prime(n):
    if n < 2:
        return(False)
    if n ==2:
        return(True)
    for d in range(2,n):
        if n%d == 0:
            return(False)
    return(True)

k = 12345

while not prime(k):
    k += 1
print(k)

## --------------------------------------------------
o =  "And there weren’t special things for kids the way there are now. Like, we would just go see movies. Any movie. Like Back to the Future. That was a movie everyone could see. Kids could kinda see it. Great movie, right? I rewatched it recently. It’s a very weird movie. Marty McFly is a 17-year-old high school student whose best friend is a disgraced nuclear physicist. And, I s you not, they never explain how they became friends. They never explain it. Not even in a lazy way, like,   Hey, remember when we met in the science building? They don’t even do that. And we were all fine with it. We were just like,   What, who’s his best friend? A disgraced nuclear physicist? All right, proceed.  What a strange movie to sell to be a family movie. Two guys had to go in and do that. They had to be like, Okay we got an idea for the next big family-action-comedy. All right, it’s about a guy named Marty, and he’s very lazy. He’s always sleeping late. Okay. Is he cool like Ferris Bueller? No. But he does have this best friend who’s, you know, a disgraced nuclear physicist.    I’m confused here. This best friend, this is another student? No, no, no. No, this guy’s either, like, 40 or 80. Even we don’t know how old this guy’s supposed to be. But one day, the boy and the scientist, they go back in time and they build a time machine. Whoa! Okay. I think I see where you’re going here. They build a time machine, and they go back in time, and they stop the Kennedy assassination. Ah! Oh, wow, that’s a really good idea, I mean, we didn’t even think of that. All right, well, what do they do with the time machine? Well, now I’m embarrassed to say. Ah, well, all right, all right, all right. We thought… We thought it would be funny, you know, if the boy, if he went back in time and, you know, he tried to f his mom. I don’t know. We thought that’d be fun for people. But, no, good point. No, he doesn’t get to, he doesn’t get to. ‘Cause this family friend named Biff, he comes in and he tries to rape the mom in front of the son. The dad’s gotta beat the rapist off of her. And also, we’re gonna imply that a white man wrote ‘Johnny B. Goode.’ So, we’re gonna take that away from ’em.    Well, this is the best movie idea I have ever heard in my life. We’re gonna make three of them. Now, you say they go to the past. How about we call it Back to the Past?    No, no, no. Back to the Future.Right, but they go to the past.Yeah."

o = o.split()
i = 0

while i < len(o):
    if o[i].lower() == "no":
        print("the no is at the " + str(i) + " index.")
        break
    print("this word is not NO.")

while i < len(o):
    if o[i].lower() == "no":
        print("the no is at the " + str(i) + " index.")
        continue
    print("this word is not NO.")

# Functions-------------------------------------
## ---def---------------------------------------
def helloWorld():
    print("hello World")

## ---Arguments---------------------------------
def helloWorld(name):
    print("hello " + name)

def helloWorld(name = "Chandler"):
    print("hello " + name)
## ---return------------------------------------
def helloWorld(name):
    return("hello " + name)

k = helloWorld
print(k)
## ---name spaces-------------------------------
#verbally explain

## --------------------------------------------------
def perfectN(n = 10):
    divs = 0
    for i in range(1,n):
        if n%i == 0:
            divs += i
    print("the sum of divisors is " + str(divs))
    if divs == n:
        return("perfect")
    elif divs > n:
        return("abundant")
    else:
        return(deficient)

#Try and Except---------------------------------
print("NO ERROR HANDLING-------------------------")
fn = int(input("what's your favorite number? "))
#what could go wrong?

print("WHILE LOOP--------------------------------")
fn = input("what's your favorite number? ")
while not fn.isnumeric():
    fn = input("what's your favorite number? ")
fn = int(fn)
#how have we fixed it in the past?

## ---try/Except----------------------------------
print("TRY EXCEPT #1--------------------------------")
try:
    fn = int(input("what's your favorite number? "))
except:
    print("That's not a number, I'll pretend you said 7.")
    fn = 7

#or
print("TRY EXCEPT #2--------------------------------")
while True:
    try:
        fn = int(input("what's your favorite number? "))
        break
    except:
        print("That's not a number")


print("\n\nFILE ISSUES-----------------------------------")
reader = open("Chelsea.txt", "r")
#what can go wrong?

try:
    filename = input("filename: ")
    reader = open(filename, "r")
except:
    print("YOU MESSED UP. GO CHECK YOUR FILE LOCATION.")

while True:
    try:
        filename = input("filename: ")
        reader = open(filename, "r")
        break
    except:
        print("YOU MESSED UP. GO CHECK YOUR FILE LOCATION.")



#List Comprehension----------------------------------------

## use LC to square the numbers in this list
f = [1,2,3,4,5,6,7]

f2 = [i**2 for i in f]

## --------------------------------------------------
a = ["A","B","C","D","E"]

b = []
for i in a:
    b.append(i.lower())
print(b)

b2 = [i.lower() for i in a]
print(b2)

## --------------------------------------------------
c = ["The quick brown fox A", "Mary had a little lamb", "New in Town"]
vows = []
for s in c:
    for letter in s:
        if letter.lower() in "aeiou":
            vows.append(letter)

print(vows)
vows2 = [letter for s in c for letter in s if letter.lower() in "aeiou"]
print(vows2)
## --------------------------------------------------

#get list of even numbers that have a 3 in them

e3s = [i for i in range(0,1000) if i%2 == 0 and '3' in str(i)]

## --------------------------------------------------

# rewrite the last example but write a function called e3check() that checks if a
# number is even and has a 3 in it. Use that in a list Comprehension.

def e3check(n):
    if i%2 == 0 and '3' in str(i):
        return(True)
    else:
        return(False)

e3s = [i for i in range(0,1000) if e3check(i)]

# Classes --------------------------------------------
class Cat:
    def __init__(self,name):
        self.name = name
        print("MEOW, I'm ", self.name)
    def meow(self):
        print(self.name + ": MEOW!")
James = Cat("James")
John = Cat("John")
James.meow()


## --------------------------------------------------

class car:
    def __init__(self,brand,model, MPG, gasTank):
        self.make = brand
        self.model = model
        self.mpg = MPG
        self.tank = gasTank
        self.oilLife = 1 #100%
        self.miles = 0
        print("CONGRATS on your new car! BEEP BEEP")
    def drive(self, miles):
        self.miles += miles
        self.tank -= miles/self.mpg
        self.oilLife -= 0.01*miles
        print("Great Trip")
    def honk(self):
        print("BEEeeeEEEEEEEP")

HondaAccord = car("Honda", "Accord", 35, 12)
HondaAccord.honk()

print(HondaAccord.mpg)
print(HondaAccord.tank)
HondaAccord.drive(100)
print(HondaAccord.tank)
