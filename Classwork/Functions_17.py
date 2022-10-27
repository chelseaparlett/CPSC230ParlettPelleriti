# Class Activities + Review (Class 17)

# Together------------------------------------------------

# 0. Questions?
# 1. How can we tell whether an object will remain changes AFTER
# a function is done running?
# 2. What type of object does a f(x) need to return to do MA?

x = []
for i in range(0,10):
    x.append(i**2)

x = []
for i in range(0,10):
    if i % 2 == 0:
        x.append(i**2)

# change into list comprehension


b = ["John", "Jacob", "Smith"]

def bff_adder(bffs, new_bff):
    bffs.append(new_bff)

bff_adder(b, "James")
print(b)

x = 2
def number_squarer(n):
    n = n**2

print(x)
# number_squarer(x)

# why does the list we put into bff_adder stay changed, but n doesnt?


def feedback_taker():
    feedback = []

    qs = ["What's one thing you enjoy about this class? ",
    "What's one thing you would change about this class? ",
    "How many hours per week do you spend on this class? ",
    "Are you taking this class as part of a requirement? "]

    for q in qs:
        answer = input(q)
        feedback.append(answer)

    return(feedback)

# what will return here?
# how many items will this list have?


tony_feedback = feedback_taker()
print(tony_feedback)

# how can i change this variable assingment to use multiple assignment?

# https://github.com/cmparlettpelleriti/CPSC392ParlettPelleriti/blob/master/Extras/ShinyHangman.ipynb

# Classwork-----------------------------------------------
'''
1. Write a function, top_3_movies() that asks the user to list their top 3
favorite movise separated by a ','. Split the string into a list of the 3
movies (assume movie titles have no commas). Loop through the list and print
a random, generic insult for each one (like "Oh, I liked that movie too...when
I was 2!"). Then return the list of 3 movies.
'''

'''
2. Call your top_3_movies function, and use multiple assignment to store the 3
movie titles in 3 separate variables, mov1, mov2, and mov3.
'''


'''
3. Make a function, item_replacer() which takes in Three arguments:
an index (i; an int), a string (s), and a list (l). The function should take the
item at index i in list l, and replace it with string s. DO NOT return anything.
Call your function as noted below. Does my_list change? Why?
'''

# to run after you create item_replacer()
# my_list = ["b", "e", "t", "t", "e", "r"]
# item_replacer(i = 1, s = "i", l = "my_list")
# print(my_list)

'''
4. Look at the function list_creator() below. Call it using the strings "c", "a",
and "p" as arguments. Does this_list exist AFTER the function has run? Print this_list
out to check. Why do you think this happens?
'''

# def list_creator(i1,i2,i3):
#     this_list = [i1,i2,i3]
#     print(this_list)

# print it out

'''
5. Write a function prime_finder() that takes in an argument n (an int), and finds
all the primes between 2 and n and returns them as a list.
'''


'''
6. Copy the code from prime_finder above, and create prime_finder2().
Add one argument, list_blank, which is an empty list. Instead of returning
the list of primes, append them to list_blank.

Call your function using the code below.

Why can we do this?
'''


# # run after defining prime_finder2()
# my_primes = []
# prime_finder2(n = 20, list_blank = my_primes)
# print(my_primes)

'''
7. 1. Write a function, go_fish(), that takes in a list, hand, of playing cards
that a person has (see below for an example of how these cards are represented).
The function should ask the user for a card type (“Which card do you want to look for?”).
Their options are [‘2’,’3’,’4’,’5’,’6’,’7’,’8’,’9’,’A’,’K’,’Q’]. The function should
then return True if they have one of those card types in their hand, and False if
they do not. 

# example of how playing cards are represented
# [‘2H’,’3H’,’4H’,’5H’,’6H’,’7H’,’8H’,’9H’,’10H’,AH’,’KH’,’QH’,
# ‘2C’,’3C’,’4C’,’5C’,’6C’,’7C’,’8C’,’9C’, ‘10C’,’AC’,’KC’,’QC’,
# ‘2S’,’3S’,’4S’,’5S’,’6S’,’7S’,’8S’,’9S’, ‘10S’,’AS’,’KS’,’QS’,
# ‘2D’,’3D’,’4D’,’5D’,’6D’,’7D’,’8D’,’9D’,’10D’,’AD’,’KD’,’QD’]

# ‘2H’ would be the 2 of hears. ‘QD’ would be the queen of diamonds.
# ‘9C’ would be 9 of clubs. ‘10S’ would be 10 of spades...etc.

# a hand might look like this, but could be *any* length > 1:
# hand = [’4C’,’7D’,’KS’,’6C’,’2H’]

# if you asked whether there were any 2's in hand, you would return true.
# if you asked whether there are any 8's in hand, you would return False

'''
