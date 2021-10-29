# Battlegame.py : Project 2

Using the python methods we’ve learned  so far, create a game that can be played by the user. Make sure to utilize things we’ve learned in class like functions, lists, and tuples...etc as needed to make your code simple and elegant. Please turn in **two files** to Canvas: 1) A python file with your game called `BattleGame.py`, and 2) Your filled out ReadMe.

Simple battle game:
1. (6 points) Create two lists, `player1` and `player2`.

Each list should have (in THIS SPECIFIC ORDER):
- A string representing the player's name. Choose whatever you want.
- A string representing their class (as in mage,  wizard, rogue...whatever)
- A list representing their special attack range (e.g. [10,20] if their special attack can do between 10 and 20 damage per attack.) You can choose this range how ever you'd like, as long as the range is only positive numbers.
- An integer (start it at 100) representing their health levels.
- An integer between 2 and 5 representing the cooldown for their special attack (e.g. if their cooldown is 2, they can only use their special attack after using the basic attack at least twice.) Choose whichever number you want in that range.
- An integer, (that is currently 0), and represents the number of turns since the player has used their special attack.

2. (5 points) The user will play as `player1` and the computer as `player2`. Print out a welcome message that tells the player their character's name, and class. (E.g. `"Welcome to Battledome. You're playing [name] who is a [class]!"`)

3. (3 points) Then print out a similar message telling the player who their opponent is

4. (3 points) Now we play the game! At the beginning of each round (a round includes 1 player1 turn, and 1 player2 turn), print `"ROUND [ X ]---------------------", where [ X ] is replaced by the current round #.`

5. (3 points) For each player1 turn (players switch off), Ask the user whether they want to do a basic attack or use their special attack. They should type `"basic"` for basic attack, and `"special"` for their special attack.

6. (5 points) if the player gives an input that is anything other than `"basic"` or `"special"` (any capitalization is fine), let them know, and continue to ask them for a response until they give you a valid one.

7. (8 points) Create  a function (the function should be defined at the top of your file, even though it is being described/used here.) called `player_turn()` that takes the attacker list, and the attackee list, and an argument `attack_special` that is either True or False. This function should be general enough to work for EITHER player1 or player2's turn.

  - (3 points) if the player tries to use their special attack, print out `"Special Attack Attempted."`

  - (15 points) Inside this function, if the player asks to use their special attack, check that it is not on "cooldown" (e.g. if their cooldown is 2, they can only use their special attack after using the basic attack at least twice). Print a message telling the user which attack they're using (use the format: `"[Basic/Special] Attack Used"`)

  - (8  points) If they want to use their special attack and they’re allowed to, use the python random package to generate an amount of damage using their damage range from their list (e.g. if their damage range is [10,20], generate a random amount of damage between 10 and 20 inclusive).

  - (5 points) If they don’t want to OR cannot use their special attack this round, then just have them do a basic attack that has a damage range of [0,6]

  - (3 points) Print a message that says they’ve done x amount of damage this round, and subtract that number of health points from the attackee's list and print the current health of the player to the screen.

  Use this format:
  ```
  "[attacker name] did [ x ] damage this round!"
  "[attackee name] has [health] health points left.\n"
  ```

  - (3 points) If, after subtracting the damage from the attackee, their health is below 0, set health to 0 instead.

  Make sure you *call* the `player_turn()` function for player1's turn.

8. (15  points) Now it's the computer's (player2) turn. Instead of asking for user input on whether to do a special or basic attack, randomly choose whether to do special or basic attacks using python’s random package (hint: `random.randint()`, `random.choice()`)

Call the `player_turn()` function for the player they’re playing against (player2).

9. (15 points) If at *ANY* point either players health is  <= 0, that person loses, and the other wins! Create a function called `still_alive()` that takes a players list as an argument and checks if their health is 0, if it is, return `False`. Otherwise return `True`. If their health is 0, choose a random string message (something like `"oh no, you’re dead, [player name]"` from a list you previously defined that has 6 options of death messages as strings, and print that string to  the  screen. Then end the  game. Use this function in your game code.

10. (2 points) If  your player wins (player1), print `"you win"`; If the computer (player2) wins, print `Sorry, the Other Player won..."`

EXTRA CREDIT (optional; 2 points): Create a pet character that helps your player by attacking the enemy with a basic attack with range[0,2] every turn. Print out a message saying how much damage your pet did.

Use this format:
`"[pet name] did [ x ] damage this round!"`

And include your pet's damage in when subtracting health points from the attackee.

BUT every 5 turns (a turn is: player 1 goes and then player 2 goes), print a message that your pet has gotten an energy boost and does either 10 points damage to the opponent OR 4 points of healing to you *instead* of their basic `[0,2]` attack. Use the  python package random to choose whether they heal or do the 10 point attack. Print out a message telling the user which was chosen. You should use/modify the `player_turn()` function to apply this damage.

Your opponent should NOT have a pet. Only you (player1).



Note: the python package random might help: https://docs.python.org/2/library/random.html

---

Below is a screenshot of what the first few rounds might look like when your players have the following values:

```
player1 = ["Charles",
"mage",
[20,25],
100,
2,
0]

player2 = ["John",
"wizard",
[25,30],
100,
3,
0]
```
![example](https://drive.google.com/uc?export=view&id=1goS1Se-5nSX4uvxUBKKRnGzXsAN96LUk)
