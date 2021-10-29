# in with dictionaries
grades = {"John": 97.6,
"Randall": 80.45,
"Kim": 67.5,
"Linda": 50.2,
"Sarah": 99.2}

## check if the student is in there
name = input("Who's grade do you want? ")

print(name in grades)

## if not there, add them
name = input("Who's grade do you want? ").capitalize()

if name in grades:
    print(grades[name])
else:
    print("This student does not have a grade for this assignment")
    g = input("Please enter a grade now: ")

    try:
        g = float(g)
    except:
        print("Invalid grade, assigning grade of 0 for now")
        g = 0
    finally:
        grades[name] = g

print(grades)

# sets
my_set = {"February", "January", "April"}
print(my_set)

my_set2 = {1,1,1,1,1,1,3,5,9,11}
print(my_set2)

# creating sets
my_list = [10,5,5,9,3,4,9,1,2,6,8,9,4,2,5,7]
my_list_to_set = set(my_list)
print(my_list_to_set)

## can't put mutable objects inside a set
my_mutables = {(1,2,3,4), (5,6,7,8)}

## but you can mix types
my_mixed_set = {1, "ant", "blue", (1,2)}
print(my_mixed_set)

# set methods
my_set.add("June")
print(my_set)

my_set.add("February")
print(my_set)

my_set.remove("January")
print(my_set)

## union, intersection, difference

odds = {1,3,5,7,9}
evens = {2,4,6,8,10}
pos_ints = {1,2,3,4,5,6,7,8,9,10}
primes = {2,3,5,7}


# union

print(odds | evens)
print(odds.union(evens))

# intersection
print(odds & pos_ints)
print(odds.intersection(pos_ints))

# difference
print(odds - primes)
print(odds.difference(primes))

print(primes - odds)
print(primes.difference(odds))

# symmetric difference
print(odds^primes)
print(odds.symmetric_difference(primes))

print(primes^odds)


# if i switched the order, would the answer be different?


'''
Let's write some code to ask two friends their favorite music artists,
and then print out a message telling them which artists they both said they like!
'''
songs = {}

for friend in range(0,2):
    f = "friend" + str(friend)

    print("Welcome " + f)

    songs[f] = set()

    artist = input("Name an artist you like, enter a blank string to end: ").lower()
    while artist != "":
        songs[f].add(artist)
        artist = input("Name an artist you like, enter a blank string to end: ").lower()

print("GREAT JOB!")
print("The artists you have in common are: ", ",".join(list(songs["friend0"] & songs["friend1"])))
