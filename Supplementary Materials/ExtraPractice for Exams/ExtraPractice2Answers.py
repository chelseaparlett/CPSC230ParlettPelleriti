#YAHTZEE
# Write a script that will roll 5 separate dice.
#Store these values and check if it's a "Yahtzee"
#(where all the dice are the same). If it is
# Print "YAHTZEEEEEEEE!"
#---------YOUR CODE HERE----------------------
import random
rolls = [random.randint(1,6) for i in range(0,5)]#list comprehension
#you can also use the commented code to do this...
#rolls = [random.randint(1,6),random.randint(1,6),random.randint(1,6),
#random.randint(1,6),random.randint(1,6),random.randint(1,6)]
yahtzee = True
for roll in rolls:
    #if they're all the same, then the 2nd-5th number
    #will be the same as the first
    #if its not a yahtzee, at least one of the 2nd-5th
    #numbers will be different from the first
    if roll != rolls[0]:
        yahtzee = False
if yahtzee:
    print("YAHTZEEEEEEEE!")
#---------------------------------------------
# TIC-TAC-TOE
# Using the below list
TTT = [
["X","O", "X"],
["X","X", "O"],
["O","O", "X"]
]
#Write a piece of code that checks if a person
#has gotten at least one 3 in a row
# Horizontally Vertically, or Diagonally.
# HINT: Checking horizontally is easy...but if someone
#had 3 in a row VERTICALLY, would all the spaces have the same index?
# REMEMBER: to get the top left "X" from TTT I use TTT[0][0]. To
# get the middle "X" I use TTT[1][1].

#Also check if it worlks for this one:
TTT2 = [
["O","O", "X"],
["X","X", "O"],
["O","X", "X"]
]
#or this one
TTT3 = [
["O","O", "O"],
["O","X", "X"],
["O","X", "X"]
]
#---------YOUR CODE HERE----------------------
ThreeinaRow = False

#CHECK Horizontally
for row in TTT:
    if row[0] == row[1] and row[1] == row[2]:
        ThreeinaRow = True
#CHECK Vertically
for i in [0,1,2]: #for each column, 0,1,2
    if TTT[0][i] == TTT[1][i] and TTT[1][i] == TTT[2][i]:
        ThreeinaRow = True
#CHECK Diagonally
if TTT[0][0] == TTT[1][1] and TTT[1][1] == TTT[2][2]:
    ThreeinaRow = True
if TTT[0][2] == TT[1][1] and TTT[1][1] == TTT[2][0]:
    ThreeinaRow = True
if ThreeinaRow:
    print("3-in-a-row")
else:
    print("TIE")
#---------------------------------------------
# GUESSING
#Randomly Generate 10 numbers between 1 and 1000 and store them
#in a list
#ASk the user to guess a number between 1 and 1000
#if their number is in the list, tell them "YAY", otherwise
#print "NOOOOO"
#---------YOUR CODE HERE----------------------
numList = [random.randint(1,1000) for i in range(0,10)]
#or
# numList = [random.randint(1,1000),
# random.randint(1,1000),
# random.randint(1,1000),
# random.randint(1,1000),
# random.randint(1,1000),
# random.randint(1,1000),
# random.randint(1,1000),
# random.randint(1,1000),
# random.randint(1,1000),
# random.randint(1,1000)
# ]
guess = int(input("Guess a Number between 1-1000: "))

if guess in numList:
    print("YAY")
else:
    print("NOOOOOOOO")
#---------------------------------------------
#GO FISH (1 round)
#Use this list of CARDS
import numpy as np
cards = ["A","K","Q","J","10","9","8",
"7","6","5","4","3","2"]
suits = ["H","S","C","D"]
Cards52 = [(card + suit) for card in cards for suit in suits]
#Use these two hands I created. OpponentHand is a list of cards.
#Try printing it!
OpponentHand = np.random.choice(Cards52,5, replace = False)

#Ask the User which card (["A","K","Q","J","10","9","8",
#"7","6","5","4","3","2"]) they want to ask the opponent for.
# store it in the variable check.
#Then go through OpponentHand to see if they have any of that
#card. Let the player know the outcome.
#for example, if you ask for A (aces), then check if there are aces
#in OpponentHand.
#---------YOUR CODE HERE----------------------
print(cards)
check = input("WHICH CARD do you want to ask for? choices above: ")

have = False
for card in OpponentHand:
    if check in card:
        have = True

#just to check...
if not have:
    print("GO FISH")
else:
    print("Have")
print(OpponentHand)
#---------------------------------------------




#---------------------------------------------
