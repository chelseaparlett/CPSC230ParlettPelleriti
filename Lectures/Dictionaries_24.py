'''Create a dictionary called Tamagotchi. It should have the keys health, love, hunger, thirst, play, and tired. Write 4 functions that act on this dictionary.
* -- medicine() should increase the health of the Tamagotchi dictionary by n (an argument that tells you how many health points to add).
* -- sleep() should decrease the tiredness of the Tamagotchi dictionary by 10 for each hour (an argument for sleep()) the Tamagotchi sleeps. Tiredness can't go negative.
* -- walk() should take distance in miles as an argument. Increase the love, hunger, and thirst in the Tamagotchi dictionary.
Increase love by 2 for every mile walked. Increase hunger by 10 for every mile walked, and increase thirst by 5 for every mile walked.
* -- feed() should take in an argument for number of cups of food given. Decrease hunger by 10 for every cup of food given.
* all Tamagotchi functions should have default arguments.
'''

Tamagotchi = {"health": 0,
"love": 0,
"hunger": 0,
"thirst": 0,
"play": 0,
"tired": 100}

def medicine(tama, n = 100):
    tama["health"] += n
    print("You were healed " + str(n) + " health!")

# medicine(Tamagotchi,100)
# print(Tamagotchi)

def sleep(tama, hours = 0):
    tama["tired"] -= (hours*10)
    if tama["tired"] < 0:
        tama["tired"] = 0
    print("You seem well rested now!")

# sleep(Tamagotchi,2)
# print(Tamagotchi)

def walk(tama, miles = 0):
    tama["love"] += miles * 2
    tama["hunger"] += miles * 10
    tama["thirst"] += miles * 5
    print("What a great walk!")

walk(Tamagotchi,3)
print(Tamagotchi)

def feed(tama,cups = 0):
    tama["hunger"] -= cups * 10
    if tama["hunger"] < 0:
        tama["hunger"] = 0
    print("What a great meal!")

feed(Tamagotchi,1)
print(Tamagotchi)

'''
Create a dictionary called student. It should have the keys: name, age, major, minor,
classes_current, classes_all, and clear_status.

Write the following functions:
-- rename() which takes in the dictionary, and a variable, new_name. Replace their
current name with new_name.
-- end_semester() which takes in the dictionary, and which moves all their current
classes to their list of ALL classes, and empties current classes.
-- major_declare() which takes in their dictionary, and a string, major, and
updates their major.
-- minor_declare() which does the same thing, but for minor.
-- covid_clear() which takes in the dictionary, and a boolean, survey, which
indicates whether or not the student has said "no" to all the covid screening
questions on their daily survey. It then changes their status to "CLEAR" or
"NOT CLEAR" based on the survey.
'''

student = {"name": "",
"age": 0,
"major": "",
"minor": "",
"classes_current": ["CPSC392", "CPSC230", "CPSC 298"],
"classes_all": [],
"clear_status": "CLEAR"}

def rename(s, new_name):
    s["name"] = new_name
    print("We've updated your records to reflect your new name!")

rename(student,"Jenna")
print(student)

def end_semester(s):
    s["classes_all"] += s["classes_current"]
    s["classes_current"] = []
    print("Great job this semester!")

end_semester(student)
print(student)

def major_declare(s, major):
    s["major"] = major
    print("Your major is now: " + major)

def minor_declare(s, minor):
    s["minor"] = minor
    print("Your minor is now: " + minor)

major_declare(student, "Enviromental Science")
minor_declare(student, "Data Analytics")
print(student)

def covid_clear(s, survey):
    if survey:
        s["clear_status"] = "CLEAR"
    else:
        s["clear_status"] = "NOT CLEAR"
    print("Thats for filling out your survey.")

covid_clear(student, survey = False)
print(student)
