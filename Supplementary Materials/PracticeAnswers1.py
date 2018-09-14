# Write a script that checks every character in a string given by the user
# and keeps a count of all the vowels. When you're done counting, print out the
# number of vowels. If the number is odd, also print "The number of vowels is odd."
#-------------------------------------------------------------------------------
#YOUR CODE HERE
user_string = input("give me a sentence: ")
vowels = 0
for char in user_string:
    if char in "AEIOUaeiou":
        vowels += 1
print(vowels)
if vowels%2 != 0:
    print("The number of vowels is odd.")

#-------------------------------------------------------------------------------
# Write a "space count" script that takes in user input (as them to write a sentence)
# and counts the number of spaces (use " ") in that sentence. Then ask them if they'd
# like to include another sentence. If they say yes, repeat the above process. If they
# say no, print out the space count.
#-------------------------------------------------------------------------------
#YOUR CODE HERE
user_string = input("give me a sentence: ")
spaces = 0
answer = "Y"
while answer == "Y":
    for char in user_string:
        if char == " ":
            spaces += 1
    answer = input("Would you like to add a sentence? Y for yes, N for no  ")
    if answer == "Y":
        user_string = input("give me a sentence: ")
print(spaces, "spaces.")

#-------------------------------------------------------------------------------
# Ask the user for two numbers, a and b. Then check whether a/b is larger, or
# smaller than 2.5, if it is larger, print "larger". Otherwise print nothing.
#-------------------------------------------------------------------------------
#YOUR CODE HERE

a = float(input("give me a number: "))
b = float(input("give me another number: "))
if a/b > 2.5:
    print("larger")
#-------------------------------------------------------------------------------
#Write a script that will keep asking the user for a number until they guess 42.
#Once they guess 42, tell them "goodbye"
#-------------------------------------------------------------------------------
#YOUR CODE HERE
num = float(input("number: "))
while num != 42:
    num = float(input("number: "))
print("goodbye")
#-------------------------------------------------------------------------------
