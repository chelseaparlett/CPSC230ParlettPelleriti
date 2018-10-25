#MUTABLE OBJECTS

def petAdder(dict):
    name = input("What's  your name ")
    pet = input("What's your pet's name")
    if name in dict:
        print("You're already in here so...")
    else:
        dict[name] = pet

d = {}

i = 0
while i < 3:
    petAdder(d)
    i += 1

print(d)

#---------------------------------------------
def birthday(my_age):
    print("INSIDE LOOP  NOW---------------------------")
    print("I'm", my_age)
    my_age += 1
    print("NOW I'm", my_age)
    print("ENDING  LOOP-------------------------------")


my_age = 80
print(my_age)

birthday(my_age)

print(my_age)
#---------------------------------------------
def birthday(my_age):
    print("INSIDE LOOP  NOW---------------------------")
    print("I'm", my_age)
    my_age += 1
    print("NOW I'm", my_age)
    print("ENDING  LOOP-------------------------------")
    return my_age

my_age = 80
print(my_age)

my_age = birthday(my_age)

print(my_age)
#---------------------------------------------
