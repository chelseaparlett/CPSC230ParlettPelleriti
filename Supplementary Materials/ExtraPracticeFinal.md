1. Write a function, *SATscore()* which takes in as an argument a list of correct answers (answers can be "A", "B", "C", "D", or "E") and a list of the user's answers, and scores the test. Return a tuple of the raw score (how many they got right), and a percentage score (what percentage they got right). This function should work for any length lists, as long as they are the same length (make sure you check that in your function!)

```
#YOUR CODE HERE

```
2. Write a function, *anagramSolver()* that takes in a string as an argument, and returns a list of EVERY possible arrangement of the letters (you could use this to solve anagrams because you could look through all the arrangements and see which one is a real word!). For example, if the argument string was "cat", this function should return ["cat","cta", "tac", "tca", "act", "act"]. This needs to work for any string with 3 characters. Try to do this without hardcoding each of the 6 possible answers, think loops.

```
#YOUR CODE HERE

```
3. Write a function, *grade_calc()* which takes in a dictionary something like this: {"exams": {"grade": 90, "weight": 40},"quizzes": {"grade": 85, "weight": 20},"homework": {"grade": 85, "weight": 40}} (although it should work if there is a different number of categories.). First, check if the weights add up to 100%, if they do not, print a warning message and return 0. Otherwise, use the weights and the grades to calculate the overall grade in the course and return it. (In the dictionary example I gave, the final grade would be an 87%)
```
#YOUR CODE HERE

```
4. (WARNING: this is very difficult, the test wont be this hard, but this is good practice!) Write a function, *battleship()* which runs a very simple game of battle ship. It takes in two arguments, a list of lists for User1, and a list of lists for User2 (see below for example). 1's represent a space where there is a ship, O's represent somewhere where there is NOT a ship. Run a game of battle ship in which each user alternates guessing the row (0-5) and column (0-5) where they think the opponent's ship is. Check the opponent's grid, and print a statement telling the user whether they hit a ship or not (remember, a ship will have a 1). Then print out a grid for the user to show which places they've guessed and whether it's been a hit or a miss. Once all of an opponent's ships have been found, the game is over. Print ("GAME OVER"). Feel free to write other necessary functions to run this game.
```
#YOUR CODE HERE

#example of ship grids
U1 = [[1,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]
U2 = [[1,1,1,0,0],
      [0,0,0,0,0],
      [0,1,1,1,1],
      [0,0,0,0,1],
      [0,0,0,0,1]]
#Guessed Grid example
# guesses so far:
#   0 1 2 3 4
# 0|H H H M 0
# 1|0 0 0 0 0
# 2|0 0 0 0 0
# 3|0 0 0 0 0
# 4|0 0 0 0 0
# H's are Hits, M's are Misses, 0's haven't been guessed yet.
```
