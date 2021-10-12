# INSTRUCTIONS

## PIG.py

## PIG Description
The game of Pig is a simple two-player dice game in which the first player to reach
50 or more points wins. Players take turns. During their turn a player can choose to roll
a 6 sided die, or hold (end their turn). After each roll:

<br>
a) If the player rolls a 1 then the player loses all their points for *this round* (NOTE: not all their points total) and it becomes the other player’s turn.
<br>
b) If the player rolls 2-6 then they can choose to either roll again or hold. If the player
holds the sum of all rolls for this turn is added to their score and it becomes the other player's turn.
<br>
<br>

Write a program that plays the game of Pig where one player is human and the
other is the computer. The game should end when one player (either human or computer)
gets 50 or more total points. When the game ends, print out a congratulations to whoever won (computer or human).

## Human's Turn
When it is the human’s turn the program should print out "HUMAN'S TURN" and then clearly show the current score of both players.

Ask the human to input “r” for roll and “h” for hold. (Hint: use the input function).
For each roll they make, print out "You Rolled a " and what they rolled.

IF the human wins on their turn the computer should NOT get a turn after that.
## Computer's Turn
When it is the computer’s turn, you should print out "COMPUTER'S TURN" and then clearly show the current score of both players.

You need not to ask the computer to roll or hold. Simply keep rolling
until the computer has earned 20 or more points and then hold. Remember, if the computer
rolls a 1 at any time during it's turn then the turn is lost and no points are added to the computer's total score.

For each roll they make, print out "You Rolled a " and what they rolled.
<br>

## General
Allow the human player to roll first. A random roll can be simulated with a call to
random.randint(1,6) which generates a uniform random integer in [1,6]. Make
sure to import the random module (ie. import random).

```
import random

roll = random.randint(1,6)
```


The image below shows what the first 2 rounds (human AND computer) of Pig might look like:

![](https://drive.google.com/uc?id=1_oFOiFpOK4zs1iejqf25fJSY10M3k4Bs)
