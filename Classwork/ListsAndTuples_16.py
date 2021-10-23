# Class Activities + Review (Class 16)

# Together------------------------------------------------

# 0. Questions?
# 1. modifying vs. nonmodifying


'''
Modify your bridge_crosser() function *again* (from the last classwork),
so that it returns a list with two things:
at index 0, it returns the # of successful steps,

and at index 1, it returns a list of the successful steps made
(e.g. ["l", "r", "l", "l"]).

So the output of the function could look something like this if the player made
4 successful steps:

# output
[4, ['l', 'r', 'r', 'r']]

'''

# let's talk about how we formed bridge!

import random

def bridge_crosser():

    # list of 0's and 1's, 1 means right side is solid,
    # 0 means left side is solid
    bridge = [random.randint(0,1) for i in range(0,10)]
    print(bridge)

    # your code here #
    safe_steps = 0
    for pane in bridge:
        choice = input("Would you like to go left or right?").lower()

        if choice == "r" and pane == 1:
            print("PHEW, safe")
            safe_steps += 1
        elif choice == "l" and pane == 0:
            print("PHEW, safe")
            safe_steps += 1
        else:
            print("Oh no, you fell")
            break
    else:
        print("CONGRATUALTIONS! You Made it Out.")
    return(safe_steps)

# Classwork-----------------------------------------------
'''
1. Let’s continue our work from Classwork 13 (Functions) and help our adventure
hero carry items.

- Make an empty list called backpack
- Make an empty list called pockets
- Create a maximum number of items for pockets and backpack (pocket max is
4 items, backpack max is 20 items) and store them in the variables
pocket_max and backpack_max.
- Create a function, storage_check() that takes in the pocket list, the backpack
list, and an item as a string. The function should check whether the pocket is
full (use len()), if it is, put item in backpack, if backpack is full, print
out the items in the backpack and ask user to choose item to remove. Once they
choose a valid item (check if they did using in), remove it and insert the new
item in its place.
- Using append, add 20 items to your backpack list.
'''

'''
2. Using the code from #1, let's have our adventurer find an apple, decide whether
to pick it up, and then eat it.

First, print out apple_message using the adventure_mess() function from Lecture 13.
Next, ask the user to input a "yes" or "no" about whether or not to pick up the apple.
Then, if they say yes, use the storage_check function to help them add the apple. If
they say no, then print out "moving on".
'''
apple_message = "You've found an apple on the ground. It looks delicious."

'''
3. Write a function, cursed_backpack() which takes in the backpack list and
performs a curse on it! The curse takes the name of each item in the backpack,
and scambles it so that it's an anagram of the item name. Return the new cursed
backpack list.
'''

'''
4. Write a function, drop_it_all() which takes in the backpack list and removes
all the items from the backpack using .pop() and prints out a message telling
the user what was removed at each iteration.
'''

'''
5. Modifying the bridge_crosser() function we made at the beginning of class
(also in the previous classwork), modify the function yet *again* so that it takes
in two arguments, known_steps, which is a list of steps the player KNOWS to be safe
(because they saw the previous player take them), and bridge, which is a list of 0's
and 1's that represent whether the right (1) or left (0) pane is the solid one.

(note: we previously created this list INSIDE the function, so remove that code. We
will now take in bridge as an argument.)

The default for this list should be [].

If the list contains any steps (e.g. it's not empty), use those steps first
and THEN ask the player to choose left or right ('l' or 'r') once that list runs out.

For example, if the playe knows the first 3 steps are ['l', 'r', 'l'], have them take
those steps, and then on the 4th step (when we don't know which is safe) ask them to choose 'l' or 'r'.
'''

'''
6. Turn the following for loops into list comprehensions
'''

l = []
for i in range(0,10):
    l.append(i**2)


for person in people:
    print(person + " is silly")


def perfect(n):
    factors = 1

    for i in range(1,n):
        if n%i == 0:
            factors *= i
    if factors == n:
        return(True)
    else:
        return(False)

is_perf = []
for j in range(1,26):
    is_perf.append(perfect(j))
