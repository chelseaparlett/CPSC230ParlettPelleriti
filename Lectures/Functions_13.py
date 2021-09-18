# function syntax

def name_printer(name):
    print("Hello " + name)


def squared(n):
    return(n*n)

# why won't this print?!?
def name_printer(name):
    print("Hello " + name)


# more functions
def name_printer2(name):
    names = name.split()
    print(names[1] + ", " + names[0]) # print last, first

# name spaces

x = 5

def addOne(n):
    x = n + 1
    print("X is", x)

print("X is", x)
addOne(x)
print("X is", x)

## add a return

x = 5

def addOne(n):
    x = n + 1
    print("X is", x)
    return(x)

print("X is", x)
x = addOne(x)
print("X is", x)

# more functions

def greaterThan10(n):
    if n > 10:
        return(True)
    else:
        return(False)

# Adventurer
'''
Make a function adventure_mess() that takes a string message to your player and formats it as below

Adventurer: <message>
'''

def adventure_mess(message):
    print("Adventurer: " + message)
