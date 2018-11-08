1. Write a Function called d20() which "rolls" a 20 sided die to set the stats of a character (dexterity, stealth, wisdom, strength, intelligence) in a dictionary called characterStats (which is an argument in the function). Character stats should have the keys name, dexterity, stealth, wisdom, strength, intelligence.
```
#YOUR CODE HERE
```
2. Write a function called insultGenerator() that takes 3 arguments: a list of adjectives, a list of nouns, and a name (like "Chelsea"). Randomly select two adjectives, and a noun, and generate a sentence that insults the user by name (use the function argument, NOT input() to get the name). Then return that sentence. Insults should be strings like "You are an utterly ugly and stupid pine tree!". Set Default arguments for all arguments. Practice calling your function with defaults.
```
#YOUR CODE HERE
```
3. Write a function called fileAlpha() that takes a filename as an argument. Open the file INSIDE THE FUNCTION, then print the words in that file one by one in alphabetical order. Also return a list of the words in alphabetical order. Assume
the only punctuation periods and commas, which you should get rid of.

```
#YOUR CODE HERE
```
4. <p> Write a function called wheelOfFortune() that takes in a string called clue, and a string called answer. Your job is to write a function to help play a round of Wheel of Fortune. Create a dictionary for the player (we're only using 1 player). The dict should store at least their name, and their money<p>

<p>Print out the clue for them to see. Then, using input() give the player a chance to guess a letter. Randomly select a price for that letter between $1 and $100 and store it in a variable, x. Count the number of times that letter appears in the answer, print out the answer, but ONLY show spaces (assume there's no punctuation, and all letters are UPPER case) and the letters that have been guessed so far. So if the answer is "Beaches" and the player guesses 'e', then you'd print out "\*e***e* ". Don't let them guess something that's already been guessed. Then award the player x dollars per number of times their letter showed up. In this case, you'd award them `2*x` dollars. </p>

<p> Then ask for their guess of the clue. If they get it right, end the game and print out a congratulatory message. If they don't get it right. Ask them for a new letter and repeat the above process. But remember, you have to show ALL the letters they guessed so far. So if on their second turn they guess 'b', you wouldn't just show "b******" you'd show "be***e*". (HINT: since you're doing this part over and over again...perhaps you need to write ANOTHER function to use here....)<p/>.

<p> End the game once they've correctly guessed the phrase. If you want more file practice, try using a file to store the correct answer and importing it!  </p>
```
#YOUR CODE HERE
```
