# basic try and except
num_not_found = True

num = input("Please give me a non-zero, positive integer: ")
while num_not_found:
    # if not num.strip("-").isnumeric():
    #     print("oh no that's not a good number!")
    #     num = input("Please give me a non-zero, positive integer: ")
    # elif int(num) <= 0:
    #     print("oh no that's not a good number!")
    #     num = input("Please give me a non-zero, positive integer: ")
    # else:
    #     num = int(num)
    #     num_not_found = False
    try:
        num = int(num)
        print(5/num)
        num_not_found = False
    except:
        print("oh no that's not a good number!")
        num = input("Please give me a non-zero, positive integer: ")





# multiple exceptions
num_not_found = True

num = input("Please give me a non-zero, positive integer: ")
while num_not_found:
    try:
        num = int(num)
        print(5/num)
        num_not_found = False
    except ValueError:
        print("Unfortunately that is not a number at all...")
        num = input("Please give me a non-zero, positive integer: ")
    except ZeroDivisionError:
        print("That's zero...")
        num = input("Please give me a non-zero, positive integer: ")


# multiple exceptions 2
my_list = ["apple", "corn", "jam", "beets"]

def item_getter(a_list, index):
    try:
        print(a_list[index])
    except TypeError:
        print("This is not an integer?! You weirdo.")
    except IndexError:
        print("Oh, so Unfortunately that index doesn't exist")

item_getter(my_list, 20)
# raising errors
def direction_getter():
    print("Welcome! You've entered a cavern, and there are 4 hallways in front of you.")
    dir = input("Would you like to go East (E), West (W), South (S), or North (N)")
    if dir.lower() not in ["n", "s", "e", "w"]:
        print("THAT'S NOT A DIRECTION, YOU FOOL!")
    else:
        return(dir)

# now
def direction_getter2():
    print("Welcome! You've entered a cavern, and there are 4 hallways in front of you.")
    dir = input("Would you like to go East (E), West (W), South (S), or North (N)")
    if dir.lower() not in ["n", "s", "e", "w"]:
        raise ValueError("That's not a valid direction!")
    else:
        return(dir)

direction_getter()
direction_getter2()

try:
    d = direction_getter2()
except ValueError as exception:
    print(exception)
    print("I'll give you one more try..")
    d = direction_getter2()

d = "none"

while d not in list("NnEeSsWw"):
    try:
        d = direction_getter2()
    except ValueError as exception:
        print(exception)
        print("I'll give you one more try..")



# raising errors 2
def divide_5():
    num_not_found = True

    while num_not_found:
        num = input("Please give me a non-zero, positive integer: ")
        if not num.strip("-").isnumeric():
            raise ValueError("oh no! that's not a number!")
        elif int(num) <= 0:
            raise ValueError("Positive Number Expected!")
        else:
            num = int(num)
            num_not_found = False

    return(5/num)

x = divide_5()
print(x)


try:
    x = divide_5()
except ValueError as exception:
    print(exception)

# finally

try:
    #open and read file
    poem = open("my_poema.txt", "r")
    for line in poem:
        print(line)
except:
    # if file doesn't exist
    print("This file does not exist?!")
finally:
    poem.close()
