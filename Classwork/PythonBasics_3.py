# Class Activities + Review (Class 3)

# Together------------------------------------------------

# 0. Questions?
# 1. Types
# 2. Constructors

# Classwork-----------------------------------------------
'''
1. What type is x? How can we use python to check?
'''

x = 10

'''
2. Which of the types we covered (Int, Float, Boolean, String, Dict,
 List, Set) are collections? What's different about a collection?


3. The == is the "equal to" operator, and it returns True if two objects
are equal, and False if they are not (see below for examples). Add a
line of code to check if the Boolean True is equal to 1.
'''
# examples
1 == 2 # False
3 <= 10 # True

# your code here

'''
4. Use Python to cast z into a string. Print type(z) before and after making
the change.
'''

z = 156


'''
5. Print the type of each of these variables.
'''

my_int = 9
my_string = "quod erat demonstrandum"
my_list = [1,2,3,4,5]
my_dict = {"name": "Jane Doe", "age": 27}
my_set = {1,1,2,3,5,8,13}


'''
6. Print out my_set. Did it change at all? Why?
'''

# your code here

'''
7. Write some code that asks the user to guess a number between 1-10.
Cast that number to an int, and then a use boolean operation to
check if the number they guessed is 7. Print out the resulting
Boolean value (which will be True when they guessed 7, and False
otherwise.)
'''
# your code here

'''
8. Write some code that asks the user for 5 different numbers, and stores
them in the variables x1, x2, x3, x4, and x5. Use a set to create a
unique set of numbers entered (e.g. if they enter 5 twice, only count it once.)
Print out the set.
'''
# your code here

'''
9. Write some code that uses a boolean operator to check whether
7 * 2 + 4 / 9 is bigger than 9 * 10 / 2 + 3 - 4
'''

x = 7 * 2 + 4 / 9
y = 9 * 10 / 2 + 3 - 4

# your code here

'''
10. Write some code that asks the user who the first president of the 
United States was. Then check (using a boolean operator) whether their 
answer is correct.
'''
# your code here

'''
11. With your group, discuss why this code doesn't work, and what
would need to be changed to fix it.
'''

i = input("How many times did you workout this week? ")

avg = i/7

print(avg, "times a day on average! Cool!")

'''
12. Use a dictionary constructor (dict()) to create a dictionary
storing the name, age, and major, of a Chapman Student. Store that
dictionary in the variable student1.
'''
# your code here