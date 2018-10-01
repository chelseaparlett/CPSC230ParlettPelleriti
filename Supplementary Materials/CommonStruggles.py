# #Continue Vs. Break------------------------------------

# #1---------------------
# #this gives an error!
# if 10 > 5:
#     print("obviously...")
#     continue #try replacing this with break. what happens?
#     print("cool")
# #Why?
#
# #A: Because continue and break both exit out of loops
# #an if statement is not a loops
# #----------------------

# #2---------------------
# agbdf = "All Good Boys Deserve Fudge"
# #what's going to print out for each for loop?
# #why are they different?
# for char in agbdf:
#     if char.lower() == "e":
#         break
#     print(char + "|")
#
# print("\n\n\n")#to make things look pretty
#
# for char in agbdf:
#     if char.lower() == "e":
#         continue
#     print(char + "|")
# #A: they're different because the second loop uses
# #a continue. Continues allow the loop to Continue
# #running, but it won't run any more code for this
# #iteration.
# #----------------------

#While/Else----------------------------------------------

# #3---------------------
# i = 0
# #before we run this, what is the last line that
# #this code will print out? what will the value of i
# #be?
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("I ONLY RUN ONCE", i)
# #A: it will be 10. Else runs once: the first time the while condition (i <10)
# #is false.
# #----------------------

# #4---------------------
# my_string = "She turned me into a newt!"
# i = -1
# while i < len(my_string)-1:
#     i += 1
#     print("I'm on index", i)
#     print("the character here is", my_string[i])
#     if my_string[i] == ".":
#         break
# else:
#     print("Guess I'm done")
#
# #add a period between me and into in my_string. Does the else
# #statement run?
#
# #A: no. it only runs when the loop exits naturally.
#
# #Q: if you change the break to a continue, will the else run?
# #A: yes! continue just moves the loop onto the next iteration
# #it will eventually exit naturally
# #----------------------

#Nested Loops---------------------------------------------

# #5---------------------
# poemstr = '''Once upon a midnight dreary, while I pondered, weak and weary,
# Over many a quaint and curious volume of forgotten lore—
# While I nodded, nearly napping, suddenly there came a tapping,
# As of some one gently rapping, rapping at my chamber door.
# "'Tis some visitor," I muttered, "tapping at my chamber door—
# Only this and nothing more."
#
# Ah, distinctly I remember it was in the bleak December;
# And each separate dying ember wrought its ghost upon the floor.
# Eagerly I wished the morrow;—vainly I had sought to borrow
# From my books surcease of sorrow—sorrow for the lost Lenore—
# For the rare and radiant maiden whom the angels name Lenore—
# Nameless here for evermore.'''
# poem = poemstr.split("\n")
#
# for line in poem:
#     for character in line:
#         if character.lower() != character:
#             print("AHA! An UPPERCASE!", character)
# #What does the first for loop loop through?
# #A: through each "line" in the poem. but really each
# #string in the list poem
#
# #what does the second loop loop through?
# #A: each letter in each string.
#
# #what happens if I added code to break out of the second for loop
# #if I see a capital letter? Does it exit out of the first for loop?
# #A: no! Try it yourself.
# #----------------------

#Types----------------------------------------------------

# #6---------------------
# name = input("What's your name? ")
# print(type(name))
#
# num = input("What's your fave number? ")
# print(type(num))
# int(num)
# print(type(num)) #did the type of num change?
# #A: no! try it yourself.
#
# num = int(num)
# print(type(num))#how about now?
# #YES! why? because when you run int(num) it creates a NEW
# #object, a number, but we didn't store it anywhere! Since
# #strings are immutable, we can't change it. We can only create
# #a new object and store it in the same variable.
#
# #NOTE: if an object is already a string, you do not need
# #to use str() on it.
#
# #----------------------
