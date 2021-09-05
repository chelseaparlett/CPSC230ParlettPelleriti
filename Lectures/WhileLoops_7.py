# if to while

x = -6

# if
if x < 0:
    print("Your number is negative.")

#while
while x < 0:
    print("Your number is negative.")
    print("Adding 1. X is now: " + str(x))
    x += 1

print("all done! x is: " + str(x))

# while never true?
 x = 10

 while x < 0:
     print("Your number is negative.")
     print("Adding 1. X is now: " + str(x))
     x += 1

 print("all done! x is: " + str(x))

# while always true?

 x = -10

 while x < 0:
     print("Your number is negative.")
     print("Adding 1. X is now: " + str(x))
     # x += 1

 print("all done! x is: " + str(x))


# password

password = input("What's your password?")

while password != "TheBestPasswordEver230":

    print("That's incorrect")
    password = input("What's your password?")


# password 2

password = input("What's your password?")
guess_limit = 10
guesses = 0

while password != "TheBestPasswordEver230" and guesses < guess_limit:

    print("That's incorrect")
    password = input("What's your password?")
    guesses += 1


# sentinel loop

pw_not_found = True

pw = input("Please set a new password: ")

while pw_not_found:

    if pw != "ThisIsMyOldPassword123" and len(pw) > 10:
        pw_not_found = False
    else:
        print("That's a bad pw.")
        pw = input("Please set a new password: ")
