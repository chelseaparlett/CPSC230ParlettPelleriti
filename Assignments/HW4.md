Please create each of these as a SEPARATE python file. Make sure to comment your code.

# Stats.py
Write a function `MMM()` that continually prompts the user for positive integer values and stores them in a list.  You should stop prompting when the user enters a negative integer value (do not add this negative integer to the list). You can assume they'll give you at LEAST 1 positive integer, and that they'll only give you integers as input.

When the user is done entering values, you should return the list of integers they have provided in sorted order.  You should then compute the mean, median and maximum of the values in the list and print them (clearly indicate which is which) for the user to see. Please do NOT go find functions (for example, dictionaries, or functions form `numpy`, or `statistics`...etc.), do the calculations by hand (though using sum/len is fine!)

# Guess.py
Let’s make a number guessing game! You will generate a random number between 0 and 100, and ask the user repeatedly for a guess until they eventually get it. To help the user along the way, you will tell them if their current guess is higher or lower than the number they are trying to guess.

To make the program modular, here are some functions you *must* use in your program.
- `guess( )` This function asks the user for an integer and returns it. Make sure to check that what the user inputted is actually a number (though you can assume they will not give you a float.)
- `comparator( )` This function takes 2 parameters `a` and `b`. If `a` is greater than `b`, the function returns 1, if `a` is smaller than `b`, it returns -1. Otherwise it returns 0.
- `remark( )` This function takes a parameter `val`, and prints the following information depending on the value of `val`:
  - “You guessed higher!” if `val` is 1
  - “You guessed lower!” if `val` is -1
  - “You got it!” if `val` is 0

For the random number generation, you can use the random library in Python.

```
import random
num = random.randint(0,100)
```

The above code will get a random number between 0 and 100 and store it in the num variable.
After that, you just need to use the functions described above to repeatedly get a guess from the user and see if it matches num. The program ends when the user has guessed the number.
