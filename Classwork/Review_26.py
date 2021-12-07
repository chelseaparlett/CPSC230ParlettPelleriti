# CLASS 22-------------------------------------------------------------------
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

# this_string = this_string.lower()
# d = {}
# for letter in list("abcdefghijklmnopqrstuvwxyz"):
#     d[letter] = this_string.count(letter)
# print(d)
#
# s = 0
# for vowel in list("aeiou"):
#     s += d[vowel]
# print(s/5)

# CLASS 23-------------------------------------------------------------------
'''
2. Using the three list below, figure out which shows/movies are

- only on netflix and no other platform
- only on hulu and no other platform
- on both netflix and hulu
- are on netflix, hulu, and amazon_prime
- are unique to their platform (e.g. shows/movies that only appear on one platform)

'''
netflix = ["Seinfeld", "The Great British Baking Show", "The Good Place", "Greys Anatomy", "Friends",
"You", "Arrested Development", "The Witcher", "Riverdale", "Uncut Gems", "The Lorax", "Breaking Bad", "The Office"]
hulu = ["Seinfeld", "Greys Anatomy", "Friends", "The Good Doctor", "The Office", "Bob's Burgers", "Cougar Town", "The Simpsons",
"Superstore", "It's Always Sunny in Philidelphia", "Desperate Housewives", "Futurama", "Frasier", "Shrek", "Parasite"]
amazon_prime = ["Seinfeld", "Spongebob", "Dexter", "Midsommar", "The Princess Bride", "Cast Away", "The Tomorrow War", "House MD", "Fight Club",
"Mrs. Doubtfire", "The Office", "The Simpsons", "Friends"]

netflix = set(netflix)
hulu = set(hulu)
amazon_prime = set(amazon_prime)

# - only on netflix and no other platform
print("\n")
print(netflix.difference(hulu.union(amazon_prime)))

# - only on hulu and no other platform
print("\n")
print(hulu.difference(netflix.union(amazon_prime)))

# - on both netflix and hulu
print("\n")
print(netflix.union(hulu))

# - are on netflix, hulu, and amazon_prime
print("\n")
print(netflix.union(hulu).union(amazon_prime))

# - are unique to their platform (e.g. shows/movies that only appear on one platform)
print("\n")

netflix = {1,2,3,4}
hulu = {2,5,6,7}
amazon_prime = {5,4,9,8}
# this is only one way to do this
print(netflix.symmetric_difference(hulu.union(amazon_prime)) - hulu.intersection(amazon_prime))

# # CLASS 25-------------------------------------------------------------------
# '''
# 1. Let's start SUPER simple. Create a class called PlayingCard. The card should
# have two instance attributes:
# - value: (2-10, Ace, Jack, King, Queen)
# - suit: (hearts, spades, diamonds, clubs)
#
# Make sure you write an __init__ method. Inside the __init__ method, raise a
# ValueError if someone tries to create an invalid card.
#
# Then write three instance methods:
#
# - getSuit() which returns the suit of the card.
# - getValue() which returns the value of the card (in terms of blackjack).
# numbered cards (2-10) are worth their respective points. Face cards (Jack, King,
# Queen) are worth 10 points. And an Ace is worth 11.
# - __str__() (note the two underscores before and after) which returns a string
# "[value] of [suit]" (e.g. "Ace of Spades", or "Queen of Hearts"). The __str__()
# method is another special method like __init__. It tells python what to print when
# you call print(object).
# '''
# class PlayingCard:
#
#     def __init__(self, val, suit):
#             self.value = val
#             self.suit = suit
#
#             if self.value not in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "King", "Queen", "Jack"]:
#                 raise ValueError("Invalid Card Value")
#             elif self.suit not in ["Spades", "Diamonds", "Hearts", "Clubs"]:
#                 raise ValueError("Invalid Suit")
#
#
#     def getSuit(self):
#         return(self.suit)
#
#     def getValue(self):
#         vals = {"2": 2,
#         "3": 3,
#         "4": 4,
#         "5": 5,
#         "6": 6,
#         "7": 7,
#         "8": 8,
#         "9": 9,
#         "10": 10,
#         "Ace": 11,
#         "King": 10,
#         "Queen": 10,
#         "Jack": 10}
#         return(vals[self.value])
#
#     def __str__(self):
#         return(str(self.value) + " of " + self.suit)
#
# c = PlayingCard("Ace", "Spades")
# print(c)
