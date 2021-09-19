# + and *

my_list = [1,2,3,4,5]

print(my_list * 2)

my_list2 = [5,6,7,8]

print(my_list + my_list2)

## warning
print(my_list + [6])

# comparisons
[1,2,3] == [1,2,3]

[1,2,3,4] > [1,2,3,3]

print([1,5,2,2,2,2] < [1,6])

# non modifying list methods

l = ["apple", "orange", "cherry", "apple", "apple"]


# modifying list methods

## append


## pop


## insert


## remove


## sort



# functions (NOT METHODS)

## len


## min, max


## sum


## sorted



# split and join


## split/join, string methods but like, with lists


## try
'''
- Create a list of 5 words 5 letters long or longer
- Using randint(0,len(list)-1) choose a random word from your list
- Convert this string into a list
- Shuffle this list using random.shuffle(list), then join together
- Print anagram string and ask user to guess the original word
'''
import random

some_words = ["honesty",
"balloon",
"kaleidescope",
"portabello",
"balcony"
]
