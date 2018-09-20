# # STRINGS
#
# one_string = 'hello world'
#
# two_string = "hello world"
#
# three_string = '''hello
#
# world'''
# print(three_string)
# #--------------------------------
# a = "line one"
#
# b = "line two"
#
# c = "line three"
#
#
# print(a + b + c)
#
# print(a,b,c)
#
# print(a + "\n" + b + "\n" + c )
# #--------------------------------
# string = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
#
# vowel = 0
#
# for i in string:
#     if i.lower() in 'aeiou':
#         vowel += 1
# print(vowel)
# #--------------------------------
#
# string[0:5]
# string[10:30:2]
# string[::]
#--------------------------------
JM = '''I have a wife and a dog, and we just bought a house.
We have a new house. It was built in the 20s, but it was
flipped in 2014. Which means it’s haunted, but it has a lovely
kitchen backsplash. Actually, we didn’t buy a house. A bank
bought a house, and I’m allowed to keep my shirts and pants
there while I pay it off for 30 years.'''

for word in JM.split(" "): #split on the spaces to get words
    print(word)
#--------------------------------
