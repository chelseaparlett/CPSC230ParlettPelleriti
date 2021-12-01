# Class Activities + Review (Class 25)

# Together------------------------------------------------

# 0. Questions?
# 1.
# 2.
# 3.
# 4.



'''
1. Let's start SUPER simple. Create a class called PlayingCard. The card should
have two instance attributes:
- value: (2-10, Ace, Jack, King, Queen)
- suit: (hearts, spades, diamonds, clubs)

Make sure you write an __init__ method. Inside the __init__ method, raise a
ValueError if someone tries to create an invalid card.

Then write three instance methods:

- getSuit() which returns the suit of the card.
- getValue() which returns the value of the card (in terms of blackjack).
numbered cards (2-10) are worth their respective points. Face cards (Jack, King,
Queen) are worth 10 points. And an Ace is worth 11.
- __str__() (note the two underscores before and after) which returns a string
"[value] of [suit]" (e.g. "Ace of Spades", or "Queen of Hearts"). The __str__()
method is another special method like __init__. It tells python what to print when
you call print(object).
'''



'''
2. Let's create another Class called Deck. This class should have one attribute.
- cards (a list of Cards (from the PlayingCard Class))

Create an __init__ method for Deck that creates the deck of 52 cards. Each of those
52 cards should be created using the PlayingCard class.

Define an instance method, shuffle() which shuffles the order of your deck.

Define an instance method, draw(), which "deals" the last card in cards by removing
it from cards, and returning it (hint: pop).

Create a Deck object, shuffle it, and use list comprehension to draw 5 cards.
'''
import random

'''
3. Using the Deck and PlayingCard classes you defined above, make a working game of
Go Fish for 2 Players. Make sure to shuffle your deck before playing.

In Go Fish, the two players, p1 and p2, are each dealt 7 cards.


### A TURN ###
Ask the first player (p1) for input about what type of card (["2", "3", "4", "5", "6",
"7", "8", "9", "10", "Ace", "King", "Queen", "Jack"]) they want to ask for.
Continue to ask them if they give you an invalid card type.

If the *second* player (p2) has any of those cards (e.g. 2's or 7's...etc), remove all
of them from their hand and add them to the first player's hand. If they do NOT
have any of those cards, print "GO FISH" and have the first player draw 1 card
from the deck.

If the first player has all 4 of a kind (e.g. all the 2's, all the Aces...),
remove them from their hand, and add 1 to their complete_set count (because
they collected all 4 cards of that type.)

Then repeat this process for the second player, where the second player is the
one doing the asking.

During the game, if a player is left without cards, they may (when it's their turn
to play), draw from the stock and then ask for cards of that rank. If there are no
cards left in the stock, they are out of the game.

### ENDING THE GAME ###
Continue to play the game until all 13 sets of card types (["2", "3", "4", "5", "6",
"7", "8", "9", "10", "Ace", "King", "Queen", "Jack"]) have been collected by a
player.

Print out a message saying who won (a player wins by collecting more sets of
card types than the other player).



To help you out (since this is kinda tough to do in one classwork...
I made some helpful functions for you and outlined the code.)
I *HIGHLY* recommend working with your groupmates and not
trying to do this on your own.
'''

# SOME HELPFUL FUNCTIONS
def print_hand(hand):
    '''pretty printing of a player's hand'''

    print("\n")
    print("YOUR HAND------------")
    l = [str(c) for c in hand]
    [print(c) for c in sorted(l)]
    print("---------------------")
def count_type(hand, val):
    ''' count the number of cards with value == val
    in the hand
    '''
    count = [c.value for c in hand].count(val)
    return(count)

# game setup

# store card types for later use
card_types = ["2", "3", "4", "5", "6",
"7", "8", "9", "10", "Ace", "King", "Queen", "Jack"]

# create a deck
d1 = Deck()
# shuffle deck
d1.shuffle()

# create p1 and p2 hands
p1 = [d1.draw() for i in range(0,7)]
p2 = [d1.draw() for i in range(0,7)]

# initiate p1_complete_set and p2_complete_set
p1_complete_set = 0
p2_complete_set = 0


# while not all sets have been found
while (p1_complete_set + p2_complete_set) < 13:
    # p1 turn----------------------------------

    ### YOUR CODE HERE ##########################################
    # if the player has NO cards, draw 1 from d1 if there are cards left in the
    # deck, otherwise, break out of the game

    #############################################################

    # print p1's hand using print_hand()
    print_hand(p1)

    ### YOUR CODE HERE ##########################################
    # ask for a card type (card type must be one the player has)
    # until they give a valid card type
    p1_ask = input("What card do you want to ask for: ")


    #############################################################


    ### YOUR CODE HERE ##########################################
    # check if p2 has any of that card, if so add it to p1's hand
    # otherwise print GO FISH and have p1 draw a card

    #############################################################

    # remove the cards from p2 that p1 just got from them
    p2 = [card for card in p2 if card.value != p1_ask]

    # check if p1 has 4 of any card. If so, remove those cards and
    # increment p1_complete_set
    for type in card_types:
        if count_type(p1,type) == 4: # if they have all of the cards
            print("All of the " + type + "'s have been found.")
            p1 = [card for card in p1 if card.value != type] # remove cards
            p1_complete_set += 1


    # p2 turn----------------------------------

    ### YOUR CODE HERE ##########################################
    # if the player has NO cards, draw 1 from d1 if there are cards left in the
    # deck, otherwise, break out of the game
    #############################################################

    # print p2's hand using print_hand()
    print_hand(p2)

    ### YOUR CODE HERE ##########################################
    # ask for a card type (card type must be one the player has)
    # until they give a valid card type
    p2_ask = input("What card do you want to ask for: ")

    #############################################################

    ### YOUR CODE HERE ##########################################
    # check if p1 has any of that card, if so add it to p2's hand
    # otherwise print GO FISH and have p2 draw a card.
    #############################################################

    # remove the cards from p1 that p2 just got from them
    p1 = [card for card in p1 if card.value != p2_ask]

    # check if p2 has 4 of any card. If so, remove those cards and
    # increment p2_complete_set
    for type in card_types:
        if count_type(p2,type) == 4: # if they have all of the cards
            print("All of the " + type + "'s have been found.")
            p2 = [card for card in p2 if card.value != type] # remove cards
            p2_complete_set += 1

    print(p1_complete_set, p2_complete_set)


if p1_complete_set > p2_complete_set:
    print("p1 wins")
elif p1_complete_set == p2_complete_set:
    print("tie")
else:
    print("p2 wins")
