# Class Activities + Review (Class 13)

# Together------------------------------------------------

# 0. Questions?
# 1. defining functions
# 2. invoking functions/ calling functions
# 3. What happens in functions stays in functions

def add_2(n):
    n = n + 2
    print("n is " + str(n))


x = 2
print(x)
add_2(x)
print(x)

# why doesn't x change? we put it in the function and added 2???

def factor_sum(x):



# Classwork-----------------------------------------------

'''
1. Building off the adventure_mess() function we did in lecture create the
following functions:

- Make a function convert_direction() that asks the user for a direction
 they want to go (as a string, north south east or west) and returns it
 to you as 1 for north, 2 for south, 3 for east, 4 for west, and 0 if they
 enter a non-valid string.

- Make a function multi_message() that takes multiple things you want to
say to your adventurer split by a semicolon (e.g. “Hello; Welcome Adventurer;
 You are in a castle; Which direction do you want to go?”) and outputs the
 messages, each on a new line.

 - Make a function called amIDeadYet() that takes in damage (an int) and
 HP (health points; an int) and returns the new updated health after taking
 damage. Also print out a damage message of your choice.

 - Using the random package imported below, make a function called damageGenerator()
 that takes in the minimum damage (min; an int), the maximum damage (max; an int)
 and buff (buff; a float). Buff is a multiplier (e.g. 1.5x) that a player
 might have to increase their damage.

 Generate a random amount of damage to do between min and max using
`random.randint(min,max)`, and apply any buffs and return the amount of damage.
Also print a string telling the user how much damage they did.
'''
import random



'''
2. Write a function, leet_me(), that recreates the code for the leet speak problem from the
last Strings classwork, but make it into a function that takes in 1 argument (the
string) and both prints and returns the leet speak version.

133+ (leet) speak is a way of writing english using symbols to replace many english
letters. Use python to change the string below into leet speak based on the
replacements listed below. Make sure to account for capitals!

'''


'''
3. Write a function, is_prime(), that takes in a positive integer and returns True if the integer
is prime, and False otherwise (feel free to recycle code you've used to check primes
before!)


Think carefully about how we can take advantage of the behavior of return() to potentially help
simplify our code.
'''
