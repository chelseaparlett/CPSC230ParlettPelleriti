# Class Activities + Review (Class 15)

# Together------------------------------------------------

# 0. Questions?
# 1. lists
# 2. tuples
# 3. mutability

# looping through a list in a list
recipe_ingredients = [["cheese", "chicken", "tomato sauce", "basil", "breadcrumbs"],
["chickpeas", "cucumber", "tzatziki", "hummus", "tomatoes", "onion"],
["hamburger", "bun", "ketchup", "lettuce", "pickles", "mayo"],
["white beans", "celery", "diced tomatoes", "shallots", "broth"]]

# how could I grab "tzatziki" from recipe_ingredients using indexing?

# if I loop through recipe_ingredients, and print out each item, what will print out each time?

# what if I wanted to go through the ingredients instead one by one?

# how can I access "celery" from recipe_ingredients?
# I'm allergic to gluten! I need to replace "bun" with "gluten free bun". HOW!?

# Classwork-----------------------------------------------
'''
1. Create a list containing strings with the names (first middle last;
E.g. Jane Anne Doe) of the people in your group. Using a for loop, loop
through the strings, and print out their names in Last, First Middle format
(e.g. Doe, Jane Anne).
'''
[
'''
2. Turn this while loop into a for loop.
'''
i = 0
my_list = ["rain", "vans", "netflix", "pluots", "blankets", "matcha", "frasier"]
while i < len(my_list):
    print("I like " + my_list[i])


'''
3. Change the item at the 0'th index of my_list to be "sun".
'''

'''
4. Change the item at the 0'th index of my_tup to be "sun" the same way.
Does it work? Why?
'''

my_tup = ("rain", "vans", "netflix", "pluots", "blankets", "matcha", "frasier")

'''
5. Create a list of the days of the week. Using a for loop and conditionals,
write some code that prints out "Go to [building]" which tells you to go to
whichever building your first class is in that day. If you do not have classes,
print out where you should go (or if you can stay home) instead.
'''

'''
6. Using the time module and the time.sleep(1) function (which asks the computer
to wait 1 second before running the next command) to make a hide-and-seek
countdown timer. Put the number of second you want to count down in the variable
time_limit, and then use a for loop and time.sleep() to print the countdown (print
the current number, and then wait 1 second). Once the countdown finishes, print
"Ready or not, here I come!"

(you can use lists or not)
'''

import time

#example of time.sleep
print("hello")
time.sleep(1)
print("world")

'''
7. Rewrite the your countdown code as a function, count_down(), which takes in
one argument, n, the number you are counting down from (make the default 10).
'''


'''
8. Imagine a game where you are 100m above the ground on a platform. There are two columns
of 10 glass panes in front of you, 10 on the right and 10 on the left. At each of the 10 steps,
one glass pane is solid and will hold your weight. The other will break the moment you step on it,
sending you plummeting to the floor below. :(

Using the code below, finish the function bridge_crosser() which does not take in any arguments. The
code below (written for you) generates a random list of 0's and 1's, representing whether the solid
glass is on the right (1) or the left (0), and stores it in the list bridge.

Ask the user to indicate whether they want to go right ('r') or left ('l'), and at each step, tell
them whether they died or chose the solid panel and lived (SO FAR...). (Make sure that the inputted
case of the l or r doesn't matter)

If they make it across the bridge, print a congratulatory message!

'''
import random

def bridge_crosser():

    # list of 0's and 1's, 1 means right side is solid,
    # 0 means left side is solid
    bridge = [random.randint(0,1) for i in range(0,10)]
    print(bridge)

    # your code here #

'''
9. Modify your bridge_crosser() function to also count the number of successful
steps the player made, and return that integer.
'''
