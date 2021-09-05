# if elif else

# baggage check
bag_weight = 75

if bag_weight > 100:
    print("That'll be $100 extra.")
elif bag_weight > 50:
    print("That'll be $50 extra.")
else:
    print("Have a nice flight!")

# bank rewards

savings = 10000

if savings > 100000:
    print("Congrats! You're in the Platinum Tier.")
elif savings > 50000:
    print("Congrats! You're in the Gold Tier.")
else:
    print("Welcome to Python Bank!")


# and or

# friends
person_kind = True
person_fun = True

if person_kind and person_fun:
    print("Would you like to be my friend?")


# maybe you're not so picky....

if person_kind or person_fun:
    print("Would you like to be my friend?")

# and/or with comparisons

num = 17

if num > 0 and 100%num == 0:
    print("This is a very specific kind of number!")


# conditional expressions

# name check
name = "Chelsea"

if name == "Chelsea":
    print("You're the professor.")
else:
    print("You're a student.")

print("You're the professor." if name == "Chelsea" else print("You're a student."))

# Daniel Craig
day = "Sunday"

if day == "Sunday" or day == "Saturday":
    print("Ladies and Gentlemen...The Weekend.")
else:
    print("Work work work work work.")

print("Ladies and Gentlemen...The Weekend.") if day == "Sunday" or day == "Saturday" else print("Work work work work work.")
