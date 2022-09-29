# Class Activities + Review (Class 9)

# Together------------------------------------------------

# 0. Questions?
# 1. range(x,y)
# 2. collections
# 3. syntax
# 4. nested for loops


# Write some code that prints out the sum of 1 to n for every number from 2 to
# 100 using a for loop.




# Write some code that counts and prints the number of e's 
# in each of these words.
list1 = ["apple", "butter", "flour", "sugar"]



# use a for loop to print out the numbers between
# 0 to 100 (inclusive) that are divisible by 13. 



# for/else
for i in collection:
    pass
else:
    pass
# using a for loop, write some code that checks if a
# word is a palindrome. If it is, print "[word] is a palindrome",
# where [word] is the palindromic word, and exit the loop.
# if you don't find one, print "sorry"

my_list = ["keys", "wallet", "gum", "lipstick", "laptop",
"phone", "sunglasses", "tissue", "kayak", "bluefin", "racecar"]





# Classwork-----------------------------------------------
'''
1. Put the names of your groupmates in a list (example below), then use a for
loop to print out "You're a valuable human being with valid feelings, [Name]"
for each name.
'''
names = ["Chelsea", "John", "Jane", "Glenn", "Joey", "Mike"]

'''
2. Using a for loop and range(), calculate the sum of all the
even numbers between 1 and 255. Print out the result.
'''

'''
3. Using a for loop, count the number of a's, e's, i's, o's, and u's in
a string that you ask the user to input. Then print out a sentence that
tells the user the counts.
'''

'''
4. A perfect number is defined as a number whos factors (other than itself)
add up to itself. For example, 6 is a perfect number because its factors
1,2 and 3 add up to 6.

A deficient number is one where the sum of its factors (other than itself)
is LESS than itself. For example, 8 (1,2,4), or 9 (1,3).

An abundant number is one where the sum of its factors (other than itself)
is GREATER than itself. For example 12 (1,2,3,4,6).

Write a python script that checks whether a number, x, is perfect, deficient,
or abundant.
'''

'''
5. Ask a user to input a positive integer. Continue to ask them if they give you
a float, or if they give you something 0 or negative.

Once you have their number, calculate the factorial (see: https://en.wikipedia.org/wiki/Factorial)
for each number from 1 to that number, and print it out (hint, use range()).
'''

'''
6. In our first strings classwork, we did this problem:

Ask the user to input two words of the SAME LENGTH. Using a WHILE loop, count
how many letters are the same between the two strings. For example in spam and
span, 3 of the letters (s,p,a) are the same. In the words bitter and better,
5 of the letters are the same. Print out a message telling the user how many
letters are the same.

re-write it using a for loop.
'''


'''
7. Write a for loop that loops through each letter in the string below. Your code
should replace any consonant (a non-vowel) with a "-", and print back the consonant-less
string at the end.
'''
the_string = "Head Shoulders Knees and Toes" 

'''
8. Re-write this while loop as a For Loop.
'''
i = 0
word = "fnkwejnfoijfowijoijwoeirj"
while i < len(word):
    print(word[i])
    if word[i] == "e":
        print("OH NO I'M SCARED OF E!!!!!!")
        break
    else:
        i += 1
'''
9. Use a for loop (or more than one...) to check which numbers between 2-15 (inclusive)
are prime. Remember prime numbers are ONLY divisible by 1 and themselves.
Print out "[number] prime" if a number is prime and
"[number] not prime" if it is not, where [number] is replaced by the current number
that you're checking.
'''
