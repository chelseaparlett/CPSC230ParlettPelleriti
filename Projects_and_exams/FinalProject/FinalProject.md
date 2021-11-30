# Battlegame.py : Final Project

We're going to extend the battlegame you made for Project2. Make sure to utilize things we’ve learned in class like functions, lists, dictionaries, sets, and tuples...etc as needed to make your code simple and elegant. Note that if there were any errors in your Project 2, you'll need to fix them while working on this project, as it is expected that you're building off of a correct version of Project 2 and can still lose points for things not working from Project 2. Please turn in to Canvas: 1) A python file with your game called `BattleGame.py`, 2) any csv files needed and 3) Your filled out ReadMe.

### Player Dictionaries
- (**5 pts**) instead of lists for your players, create dictionaries with the following keys:
  - *name*: A string representing the player's name. Choose whatever you want.
  - *class*: A string representing their class (as in mage,  wizard, rogue...whatever)
  - *special_attack_min*: An int representing the baseline amount of damage special attacks do. You can choose this range how ever you'd like, as long as it is a positive number.
  - *special_attack_max*: An int representing the maximum amount of damage special attacks do. You can choose this range how ever you'd like, as long as it is a positive number.
  - *health*: An integer (start it at 100) representing their health levels.
  - *cooldown*: An integer between 2 and 5 representing the cooldown for their special attack (e.g. if their cooldown is 2, they can only use their special attack after using the basic attack at least twice.) Choose whichever number you want in that range.
  - *turns_since*: An integer, (that is currently 0), and represents the number of turns since the player has used their special attack.
- (**15 pts**) Create 20 characters with at least 4 different “classes” (classes can be whatever you want, but an example of classes would be warrior, mage, healer, rogue). You should do this by creating and then reading the data in from a .csv file (each character would be a row), which we covered in class. (Note that you can’t easily read in a list for your attack range (for example, `[0,6]`, which is why we now have separate entries for `special_attack_min` and `special_attack_max`). You should then store these character dictionaries in a way that allows your player to select their character *without* you hardcoding if/elif statements for all 20 characters.
- (**7 pts**) Print the names and classes of the characters, and ask the user to input the name of the character they want to play. Continue to prompt them  for a name until they give you a valid one (case shouldn't matter). Randomly choose one of the *remaining* characters for them to play against, and print a message telling them the name and class of their opponent.
### Weapons and Armour
- (**5 pts**) In your python file (i.e.  you do not need to use a csv for this part), create a dictionary of 10 weapons that each have their own ideal class (i.e. a wand that might be best used by a mage, a sword by a warrior...etc). Each weapon, should have a dictionary that has at least the name of the weapon, damage range, and ideal class of the weapon. E.g. `{'name': 'blah', 'damage': [10,12], 'ideal': 'mage'}`
- (**5 pts**) In your python file (i.e.  you do not need to use a csv for this part), create a dictionary of 10 pieces of armor. Each piece of armor should have a dictionary that has at least the name, blocking range (a range of how many damage points it will block), and blocking_chance (a float between 0-1 representing the proportion of times the armour will block any damage). E.g. `{"name": "something", "block_range": [5,10], "blocking_chance": 0.7}`
- (**10 pts**) Print out a string that describes each weapon. Be creative with this! Make sure you tell them what class is best with the weapon. Do NOT just print out the dictionary, you need to create and format a string by pulling information from the dictionary. DO NOT hardcode description strings. After a user has selected their character, ask them to choose a weapon. Continue to ask them until they give you a valid input. Store this weapon in the player's dictionary under the key `weapon`. Randomly select a weapon for the opponent, store it in their dictionary under the key `weapon`. Again, print out a string that describes their weapon. Your player and the opponent can use the same weapon.
- (**5 pts**) Print out a string (NOT the dict) to describe each piece of armor, and ask the user to choose a piece of armour. Continue to ask them until they give you a valid input. Store armor in your player dictionary under the key `armour`. Randomly select a armour for the opponent, store it in their dictionary under the key `armour`. Print out a string that describes the armour that was chosen. Your player and opponent can use the same armour.
- (**13 pts**) When in “battle” the basic attack no longer does between `[0,6]` damage, instead we get the damage range from the damage range of the weapon they choose. If a player has a weapon that is not made for their class, the weapon does 1 point less damage per hit (still generate a random number for damage, but if their class does not match the weapon’s, subtract 1 before inflicting damage. REMEMBER that you don’t want to do -1 damage, so be careful of your numbers…) Special attacks are NOT affected by the weapon at all, they do the regular amount of damage, do not subtract 1.

### Special Attack Updates

- (**15 pts**) Speaking of special attack, let’s make ours more fun. Each special attack is now a little riskier. When someone uses their special attack, choose a random integer between 0 and 10.  If the integer is less than or equal to 2, heal the attackee 2 points instead of using the special attack. This STILL counts as using your special attack. Print a message to tell them if they healed their opponent or damaged them.
### Blocking
- (**15 pts**) Alter your current game so that each time someone attacks, the attackee has a chance of their armor blocking some of the damage. The chance of the armour blocking the damage is equal to its `blocking_chance` (e.g. if `blocking_chance` is 0.7, there should be a 70% chance that the armour blocks some damage, and a 30% chance it blocks 0 damage) The amount of damage blocked should be randomly selected from the range of the armour. Print a message telling the user how much damage was generated, and how much was blocked (e.g. `"[attaker] dealt 20 damage was dealt but [attackee] blocked 8 damage."`; where [attacker] and [attackee] are replaced with the names of the players). Then print out how much total damage was ultimately done (e.g. `"[attacker] did 12 damage this round!"` where [attacker] is replaced with the attacker's name.) Remember you can't do negative damage!

### Extra Credit

- (**2 pts**) *Extra Credit*: Use Classes to implement things in this game. You should have a class for each of the classes of character you have.  Instead of storing the character choice of the player and opponent as a dictionary, use these values to set class attributes.

    The classes should have at least an __init__() method that takes the values from a character dictionary and assigns them as attributes, a `set_weapon()` method and `set_armor()` method that adds armor/weapons to their attributes, an `attack()` method that takes the other player as an argument and works similarly to your player turn function. If you do the extra credit, you may have more questions, come ask me or shoot me an Slack.
https://www.learnpython.org/en/Classes_and_Objects
https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
https://www.codecademy.com/courses/learn-python/lessons/introduction-to-classes/exercises/why-use-classes?action=lesson_resume
https://www.programiz.com/python-programming/class


---
### Example
Below is a screenshot of what the first few rounds might look like:


![example](https://drive.google.com/uc?export=view&id=1W3SV9aCjqyFJkMTwTI2p9J1J8DPSGCXQ)
![example2](https://drive.google.com/uc?export=view&id=1YFA8V8Rix8cXvp3MSYIomSxoA8CsahYd)
