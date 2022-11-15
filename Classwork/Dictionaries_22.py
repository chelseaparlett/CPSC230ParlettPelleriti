# Class Activities + Review (Class 22)

# Together------------------------------------------------

# 0. Questions?
# 1. Indexing with Dictionaries
# 2. Adding key:value pairs
# 3. Overwriting key:value pairs
# 4. .get()
# to clarify




# # use a dictionary to store the prime factors of the numbers 4-40 where the
# # number is the key, and the value is a list of it's prime factors.
#
# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i: # if i is not a factor of n
#             i += 1 # check next number
#         else:
#             n //= i # divide n by that factor
#             factors.append(i) # add factor to list
#     if n > 1:
#         factors.append(n)
#     return factors
# d = {}



# # loop through this dictionary and print out any number that has 5 as a
# # prime factor.


# # loop through this dictionary and print out any number that does NOT HAVE 2 as a
# # prime factor.



# DictReader
import csv

b = "Beyonce_data.csv"
f = open(b, "r")

dr = csv.DictReader(f)

for row in dr:
    print(row)


# harry potter
# We're going to write a dictonary to store spells and
# How much damage they do



'''
1. Using the spells dictionary we created above, let's create a wizard battle! Make
3 dictionaries, one for Ron, and one for Harry. Include keys/values
representing their name, house (Gryffindor, Hufflepuff, Ravenclaw, Slyterhin),
their health, spells_cast (a currently empty list that will keep track of the
spells they've cast), and a key "spell_probability" that's a value between 0 and 1.

Then, use a for loop to have Ron and Harry each cast 5 spells each on each other. Ask
the user (for both Ron and Harry) which spell to use (assume correct spelling, but
any case). Then print out a message saying "casting [spell]" where [spell] is replaced
with the spell they cast. Use random.uniform(0, 1) to generate a value between 0 and 1
and ONLY cast the spell if the value is less than the persons spell_probability.
If the spell fails, print out "spell failed". Otherwise print "spell complete".

Then print a message saying how much damage was done to
the other player (e.g. if Ron is casting the spell, Harry takes the damage), and
subtract the attacked player (e.g. if Ron is casting the spell, Harry takes the damage.)

Print Harry and Ron's spells_cast.
'''




'''
2. Open a connection to the file therepublic.txt (download from GitHub under
ResourcesAndData), and use a dictionary to count the number of the following
words (case should not matter):

- and
- or
- if
- to
- of
- all
- he

(make sure you remove punctation so that something like "and," would still count.)
string.punctuation gives you a collection of all the punctuation marks.

Make sure to close your file when you're done.

'''


'''
3. Create a dictionary, alpha, whose keys are the lowercase letters of the alphabet.

Then, looping through the same file as above, add each word from the file (again,
stripping punctuation, and ignoring case) to a list associated with they key of
the letter the word starts with. So, for example "apple" would go in the list
associated with the 'a' key.

E.g. at the end, alpha could look like this (the ... represents the rest of the
dictionary):

{'a': ["apple", "all", "ambush"],
'b': ["bored", "be", "behst", "balm"],
'c': ["care", "clock", "called", "calm"]
.
.
.
'z': ["zerbra", "zoom"]}

'''
import string

# string.punctuation



'''
4. From this_string below, make a dictionary that counts the number of each letter
(a-z, case doesn't matter.). Then print out the mean count for the vowels.

'''
this_string = '''
On emerging from the Old Manse, it was chiefly this strange, indolent,
unjoyous attachment for my native town, that brought me to fill a
place in Uncle Sam’s brick edifice, when I might as well, or better,
have gone somewhere else. My doom was on me. It was not the first
time, nor the second, that I had gone away,—as it seemed,
permanently,—but yet returned, like the bad half-penny; or as if
Salem were for me the inevitable centre of the universe. So, one fine
morning, I ascended the flight of granite steps, with the President’s
commission in my pocket, and was introduced to the corps of gentlemen
who were to aid me in my weighty responsibility, as chief executive
officer of the Custom-House.

I doubt greatly—or, rather, I do not doubt at all—whether any public
functionary of the United States, either in the civil or military
line, has ever had such a patriarchal body of veterans under his
orders as myself. The whereabouts of the Oldest Inhabitant was at once
settled, when I looked at them. For upwards of twenty years before
this epoch, the independent position of the Collector had kept the
Salem Custom-House out of the whirlpool of political vicissitude,
which makes the tenure of office generally so fragile. A soldier,—New
England’s most distinguished soldier,—he stood firmly on the pedestal
of his gallant services; and, himself secure in the wise liberality of
the successive administrations through which he had held office, he
had been the safety of his subordinates in many an hour of danger and
heart-quake. General Miller was radically conservative; a man over
whose kindly nature habit had no slight influence; attaching himself
strongly to familiar faces, and with difficulty moved to change, even
when change might have brought unquestionable improvement. Thus, on
taking charge of my department, I found few but aged men. They were
ancient sea-captains, for the most part, who, after being tost on
every sea, and standing up sturdily against life’s tempestuous blasts,
had finally drifted into this quiet nook; where, with little to
disturb them, except the periodical terrors of a Presidential
election, they one and all acquired a new lease of existence. Though
by no means less liable than their fellow-men to age and infirmity,
they had evidently some talisman or other that kept death at bay. Two
or three of their number, as I was assured, being gouty and rheumatic,
or perhaps bedridden, never dreamed of making their appearance at the
Custom-House, during a large part of the year; but, after a torpid
winter, would creep out into the warm sunshine of May or June, go
lazily about what they termed duty, and, at their own leisure and
convenience, betake themselves to bed again. I must plead guilty to
the charge of abbreviating the official breath of more than one of
these venerable servants of the republic. They were allowed, on my
representation, to rest from their arduous labors, and soon
afterwards—as if their sole principle of life had been zeal for their
country’s service, as I verily believe it was—withdrew to a better
world. It is a pious consolation to me, that, through my interference,
a sufficient space was allowed them for repentance of the evil and
corrupt practices into which, as a matter of course, every
Custom-House officer must be supposed to fall. Neither the front nor
the back entrance of the Custom-House opens on the road to Paradise.
'''





'''
5. Create a dictionary with the keys, title (like Mrs. Miss, Mr. Mx...),
first_name, last_name, years_worked, job_title, pets (value should be a boolean).

Fill out the values however you want.

Then, using the email_template below, print out a customized email for an office
worker. If the worker has a pet ("pet": True), add an extra line at the end of
the template saying "P.S. I hope your pets are well too!".

'''
email_template = '''
Dear title first_name last_name ;

We wanted to reach out to you and share our genuine, and completely unforced
appreciation for the work you do at our company. You have worked for years_worked
long years as a job_title , and have made the company 100x as much money as
we've paid you! This makes us incredibly happy, and we hope to continue this
professional relationship. There's a treat in the break room for you. Truly
a pleasure to work with you, first_name .

Best,
Management
'''




'''
6. Using the dictionary below that represents the possible grade breakdown
for a course, calculate the weighted final grade for the dictionaries listed
below using this weighting:

- assignments: 40%
- participation: 15%
- challenges: 5%
- exam1: 10%
- exam2: 10%
- finalexam: 20%

'''

studentA = {"assignments": 90,
"participation": 85,
"challenges": 99,
"exam1": 87,
"exam2": 82,
"finalexam": 79}

studentB = {"assignments": 60,
"participation": 85,
"challenges": 99,
"exam1": 75,
"exam2": 75,
"finalexam": 81}

'''
7. Create a function, dictionary_maker() that takes in two arguments: keys (a list of
keys for a dictionary), and values (a list of values for the dictionary).

Raise an error if keys and values are different lengths.

Create a dictionary with the key, value pairs and return the dictionary.

Call your function.
'''

'''
8. Using csv.DictReader(), open the file Beyonce_data.csv (found under ResourcesAndData
on GitHub) and put it through csv.DictReader() which is like csv.reader but returns
rows as a dictionary, rather than a list.

Loop through the rows, and:

- calculate the mean valence for Beyonce songs
- make a dictionary of the number of times each key occurs
- count the number of times the track name contains the word you (any case)
'''

import csv
