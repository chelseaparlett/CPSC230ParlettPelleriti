# immutable objects
def my_f(x):
    print(id(x))
    x = 24
    print(id(x))

h = 2
print(id(h))
my_f(h)


mutable objects
def my_f2(x):
    print(id(x))
    x[0] = 24
    print(id(x))

h = [1,2,3]
print(id(h))
my_f2(h)
print(h)


def add_student(l, studentName):
    l.append(studentName)

students = ["Frasier", "Niles", "Daphne"]

add_student(students, "Roz")

print(students)

# returning multiples, and multiple assignment

import random

def roll_3_dice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)

    return(d1,d2,d3)


dice_tup = roll_3_dice()
print(dice_tup)

die1, die2, die3 = roll_3_dice()
print(die1)
print(die2)
print(die3)

def name_splitter(name):
    name_sep = name.split()
    return(name_sep)

their_names = name_splitter("Chelsea Mariko Parlett")
print(their_names)

first, middle, last = name_splitter("Chelsea Mariko Parlett")
print(first)
print(middle)
print(last)
