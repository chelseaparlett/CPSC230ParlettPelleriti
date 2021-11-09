# Class Activities + Review (Class 20)

# Together------------------------------------------------

# 0. Questions?
# 1. opening files
# 2. closing files
# 3. ways to open a file
# 4. looping through a file

# when you call open on a file, and then loop through it, what are we looping
# through? characters? lines? paragraphs?

# open the file Beyonce_data.csv and print out the mean danceability for her songs.
'''
1. Write a function, letter_counter() that takes in the name of a file as a string (fn),
and a letter (letter) as arguments and returns the number of times that character
occurs in the file (regardless of case).

Download the file heardofdarkness.txt from the course GitHub (under ResourcesAndData).
Read in this file using python. Count the number of c's, e's, and s's in the file.
'''


'''
2. Write a function, poem_maker() that takes in the name of a file as a string,
fn, as an argument. Set the default argument to "poem.txt".

Ask the user for one line of a poem. Add that line to the file. Repeat this
process until the user enters an empty line.

Close the file.
'''

# def poem_maker(fn = "poem.txt"):



'''
3. If you run this function twice in a row, which poem does the document contain?
The first or the second? How does this relate to whether you opened the file with
'w' or 'a'?
'''


'''
4. Read in the file "students.csv" (found on GitHub under ResourcesAndData).
This file is sorta like an excel/Sheets file.

Each line in the file represents a row, that has a bunch of different values
separated by commas (print the lines out, so you can see what they look like!
the csv in the file extension stands for comma separated values!)

This file contains the name, age, year, major, and GPA of a bunch of students. Loop
through the file and store all the ages in a list, all the years in another list,
all the majors in another list, and all the GPA's in yet another list.

Find the Mean GPA, and the mean age of these students, also count the number of
students with a w (upper or lowercase) in their names.
'''


'''
5. Your friend left you a message in the file , secret.txt! To read their message,
Grab the first word on the prime numbered lines (e.g. lines 2,3,5...) and put them
in a single string to view the message. Start counting lines at 1 not 0.
'''

'''
6. Write a function wheel_of_fortune(), which takes in a file path to a txt file, phrase, as an argument.
The file should have one line that contains a short phrase.

The function should first create a dictionary and count the number of letters (make sure to
call .lower() on  the phrase first so you don't count upper and lower case letters differently).

Then, print out a - (representing a blank space) for each letter in the phrase, like they do on wheel of fortune. Spaces
and punctuation should still be shown. For example, if the phrase was "all's well that ends well"
you should print out "---'- ---- ---- ---- ----".

Ask the user to guess a letter (including vowels, unlike wheel of fortune!). Then, using the
dictionary you made, print out a message "There are [number] [letter]'s!'" where letter is
the letter they guessed, and number is how many of that letter are in the phrase.

Then replace the -'s corresponding to those letters. For example, for the phrase
"all's well that ends well", if the user guesses a on their first try, then you'd
print out "a--'- ---- --a- ---- ----".

Then, continue to ask them for letters until they have guessed the whole phrase.
When they've guessed the phrase, print out a message congratulating them.

If at any point they guess a letter that is not in the phrase, print out a message
telling them so, but let them continue guessing.

Create your own txt file with a phrase, and test out your function!
'''

'''
7. Write a function, exclamation(), that takes in a filename, f, as an argument. The
function should then open a connection to the file, and count the number of "!" in the
file, and return that count. Make sure to close your file when you're done with it.

(you can test this with any of the book files on GitHub!)
'''
