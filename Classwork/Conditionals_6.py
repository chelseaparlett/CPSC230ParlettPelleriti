# Class Activities + Review (Class 6)

# Together------------------------------------------------

# 0. Questions?
# 1. If/Elif/Else
# 2. And/Or
# 3. Conditional Expressions

# Classwork-----------------------------------------------
'''
1. Help me figure out where to go on campus! On MW I tech in Keck.
On TTh I teach in the Library. And on Friday I work in my office in
Swenson Hall. On the weekend I am at home.

Write a python script that asks me (the user) to input
the day of the week and use ifs/elifs/elses to print out where I should
be based on what day it is (either Keck, Library, Swenson, or Home).
'''

'''
2. Create some code that checks whether a number is even.
If it is,  print "even", otherwise print "odd". If the number
is 0, print "this is neither even, nor odd".
'''

'''
3. Pretend you're writing some code for a convience store. Ask the user to
input the name of an item (such as diapers, milk, lipgloss, moisturizer...etc).
Check if the item is either "cigarettes" or "alcohol". If it is, ask the user
how old they are and make sure they're old enough to buy the item (18 for
cigarettes and 21 for alcohol). If they're not old enough, print "Sorry I can't
sell you that.", If they are old enough, OR they're buying something else, print
"Thank you for your purchase".
'''

'''
4. Ask a user to input an integer, then check if that integer is even and
greater than 17. If it is print "yes!".
'''

'''
5. Translate the following if statements into conditional expressions.
'''

# if 1
x = 10
# ------------------------------------------
if x == 7:
    print("That's a lucky Number!")
else:
    print("okay.")
# ------------------------------------------

# if 2
late_days = int(input("How many late days do you get?"))

# ------------------------------------------
if late_days == 3:
    print("Correct!")
else:
    print("WRONG.")
# ------------------------------------------

# if 3
string = "kayak"

# ------------------------------------------
if string == string[::-1]: # using [::-1] reverses a string
    print("palindrome")
else:
    print("boring old word.")
# ------------------------------------------

# if 4

x = 12
# check if number is divisible by 2 and 3.

# ------------------------------------------
if x%2 == 0 and x%3 == 0:
    print("yes")
else:
    print("no")
