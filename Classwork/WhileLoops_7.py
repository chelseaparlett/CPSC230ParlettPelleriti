# Class Activities + Review (Class 7)

# Together------------------------------------------------

# 0. Questions?
# 1. If vs. while
# 2. Sentinel Loops
# 3. Continue vs. Break

# Classwork-----------------------------------------------
'''
1. Write a program that asks the user to guess your age. If they
guess too high, print out "wow, do I look that old?". If they guess
too low, print out "hahaha don't I look wiser than that?". Once they
guess correctly, print out a message telling them and exit the loop.
'''


'''
2. Re-create and extend our password example from the lecture videos. Ask
the user to enter a potential password, and check if it meets your critera.
If their password does not meet the criteria, tell them why, and ask them
for a new password.Continue to ask them for a new password if their old one
is bad. Make sure each password:

- is at least 10 characters long
- is not "Password123"
- has an exclamation point in it (see example of in operator below)
- has no spaces (see example of in operator below)
- is less than 50 characters long
'''

# exclamation point

### EXAMPLE CODE ###
"!" in "Hello!" # this is True
"!" in "Hello" # this is False

# spaces
### EXAMPLE CODE ###
" " in "This is Boring." # this is True
" " in "ThisIsBoring." # this is False

'''
3. What's wrong with this while loop and how can you fix it?
'''

x = 1
while x < 10:
    print("smol number")
print("number is no longer smol")

'''
4. Write some code that asks the user to enter the course code (e.g. CPSC 230)
for one of their classes. Then print out "Great! [Course] sounds like a fun class!",
and ask them if they want to input another course that they're in. You should
stop asking them for course codes once they enter an empty string "" instead of
a course code (you'd do this by not entering anything in the prompt and just
pressing Enter immediately).
'''

'''
5. Using a while loop, print out all the numbers between 1 and 200 that are
divisible by both 5 and 9.
'''

'''
6. Using a while loop and continue, write some code that asks the user to input
one single letter. IF the letter is z or Z, print out "I HAVE Z's!!!", and do
not finish this iteration of the loop.

Otherwise, add the letter they've inputted to a string, my_string, that stores
all the characters they've input so far (remember the + operator for strings).
If they enter an empty string "", stop the loop. Print out my_string at the end.
'''

my_string = "" # to keep track of inputs

inputs = input("Enter one Letter") # current input


'''
7. Use a while loop and indexing to loop through the characters in a string and
count the number of e's, t's, n's, o's, r's, i's, a's, and s's. Keep each count
in it's own variable. Make sure to count both capital and lower cases as the
same letter (e.g. "a" and "A" both count as an a.)
'''

the_string = '''Brave Sir Robin ran away. Bravely ran away away. When danger
reared it's ugly head, he bravely turned his tail and fled. Brave Sir Robin
turned about and gallantly he chickened out'''



'''
8. Ask the user to input two words of the SAME LENGTH. Using a WHILE loop, count
how many letters are the same between the two strings. For example in spam and
span, 3 of the letters (s,p,a) are the same. In the words bitter and better,
5 of the letters are the same. Print out a message telling the user how many
letters are the same.
'''
