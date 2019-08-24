#YAHTZEE
# Write a script that will roll 5 separate dice.
#Store these values and check if it's a "Yahtzee"
#(where all the dice are the same). If it is
# Print "YAHTZEEEEEEEE!"
#---------YOUR CODE HERE----------------------
import random
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

#---------------------------------------------
# GUESSING
#Randomly Generate 10 numbers between 1 and 1000 and store them
#in a list
#ASk the user to guess a number between 1 and 1000
#if their number is in the list, tell them "YAY", otherwise
#print "NOOOOO"
#---------YOUR CODE HERE----------------------

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

#---------------------------------------------
