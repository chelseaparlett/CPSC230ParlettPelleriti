# INSTRUCTIONS

## PIG.py
The game of Pig is a simple two-player dice game in which the first player to reach
100 or more points wins. Players take turns. On each turn a player rolls a six-sided
die. After each roll:
<br>
a) If the player rolls a 1 then the player gets no new points and it becomes
the other player’s turn.
<br>
b) If the player rolls 2-6 then they can either roll again or hold. If the player
holds the sum of all rolls is added to his/her score and the turn passes to the
other player.
<br>
<br>
Write a program that plays the game of Pig where one player is human and the
other is the computer. When it is the human’s turn the program should show the
score of both players and the previous roll. Allow the human to input “r” for roll
again and “h” for hold. (Hint: use the input function).
When it is the computer’s turn you need not do any prompting. Simply keep rolling
until the computer has earned 20 or more points and then hold. If the computer
rolls a 1 at any time then the turn is lost and no points are added to the score. If at
any point the computer has enough points to win the game then the computer holds
and the game ends.
<br>
Allow the human player to roll first. A random roll can be simulated with a call to
random.randint(1,6) which generates a uniform random number in [1,6]. Make
sure to import the random module (ie. import random).

```
import random

roll = random.randint(1,6)
```

## COUNTER.py
Write a Python function that takes a list of words and returns the length of the longest one.