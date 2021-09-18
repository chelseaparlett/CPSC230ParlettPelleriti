# default arguments
def menu_printer(item = "Turkey Sandwhich"):
    print("You're having the " + item + " today! Enjoy.")

menu_printer()
menu_printer("Impossible Burger")
menu_printer(item = "Eggplant Parmesean")

# named arguments
def three_things(thing1, thing2, thing3 = "you"):
    print("Here are 3 things I love:\n" + thing1 + ", " + thing2 + ", " + thing3)


three_things("eggs", "butter", "lamps")
three_things("the sun", "jelly")
three_things(thing2 = "John Mulaney", thing3 = "black licorice", thing1 = "jam")
three_things("olive oil", thing2 = "blood")

def three_things(thing1 = "sunshine", thing2 = "water", thing3 = "you"):
    print("Here are 3 things I love:\n" + thing1 + ", " + thing2 + ", " + thing3)

three_things(thing2 = "orange juice")
# more function practice

def store(shirt_price = 7.99, shirt_bought = 0,
 shoe_price = 20.99, shoe_bought = 0,
  socks_price = 2.99, socks_bought = 0,
   tax = 0.08):
    total = (shirt_price * shirt_bought) + (shoe_price * shoe_bought) + (socks_price * socks_bought)
    total = total * (1 + tax)
    return(total)

print(store(shoe_bought = 2, shoe_price = 15.75))

# more more function practice
def upperCounter(s = "The Quick Brown Fox"):
    count = 0
    for letter in s:
        if letter.isupper():
            count += 1
    return(count)

print(upperCounter(s = "HELICOPTER"))

# more more more function practice
def prime(n):
    if n == 1:
        return(False)
    elif n == 2:
        return(True)
    else:
        for x in range(2,n):
            if n%x == 0:
                return(False)
        return(True)
print(prime(12))
