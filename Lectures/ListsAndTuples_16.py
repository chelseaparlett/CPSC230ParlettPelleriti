# + and *

my_list = [1,2,3,4,5]

print(my_list * 2)

my_list2 = [6,7,8,9]

print(my_list + my_list2)

## warning

print(my_list + 6)


# comparisons

[1,2,3] == [1,2,3]

[1,2,3,4] > [1,2,3,3]

[1,5,2,2,2,2] < [1,6]

# non modifying list methods

l = ["apple", "orange", "cherry", "apple", "apple"]

l.count("apple")

l.index("orange")

# modifying list methods

## append
l.append("cherimoya")

print(l)

## pop
popped_element = l.pop(0)
print(l)
print(popped_element)

## insert
l.insert(0, "apple")
print(l)

## remove

l.remove("orange")
print(l)

l.remove("apple")
print(l)

## sort

m = [4,3,2,6,7,8]
m.sort()
print(m)


# functions (NOT METHODS)

## len
print(len(m))

## min, max
print(min(m))
print(max(m))

## sum
print(sum(m))

## sorted
print(sorted(m))
print(m)



# split and join

## split/join, string methods but like, with lists
our_words = "It is a truth universally acknowledged".split(" ")
print(our_words)

our_variable = "_".join(our_words)
print(our_variable)

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

i = random.randint(0,len(some_words) - 1)
word = some_words[i]

word = list(word)
random.shuffle(word)

word = "".join(word)
print(word)
