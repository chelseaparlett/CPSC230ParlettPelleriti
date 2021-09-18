# immutable objects

def my_f(x):
    print(id(x))
    x = 24
    print(id(x))

h = 2
print(id(h))
my_f(h)


# mutable objects

def my_f2(x):
    print(id(x))
    x[0] = 24
    print(id(x))

h = [1,2,3]
print(id(h))
my_f2(h)



def add_student(l,studentName):
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

    return (d1,d2,d3)

dice_list = roll_3_dice()
die1, die2, die3 = roll_3_dice()


def name_splitter(name):
    name_sep = name.split()
    return(name)

name_list = name_splitter()
first, middle, last = name_splitter()
