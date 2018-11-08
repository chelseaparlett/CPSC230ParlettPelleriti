def saleMaker(item = "apples", percent = 0.25, inventory = {"apples": 10.5}):
    inventory[item] = round(percent* inventory[item],2)
    print(inventory)
    percent = percent + 0.2 #get rid of stock
    return percent

#i = {"apples": 2.45, "plumbs": 10.10, "almonds": 100.25}

nprice = .5
#print("BEFORE:",i, nprice)
saleMaker()
#print("AFTER:",i,nprice)
#How can I change my code to automatically take 25% as the default price?
# How about the default item and dict are "apples" and {"apples": 10.5}

# Call saleMaker using all defaults, and with NO defaults.
# What if you just want to use the percent default?
#--------------------------------------------------
# Write a function prime, that has the default argument 100
# Call it using the default arguments, call it using 10
def prime(n = 100):
    p = True
    for x in range(2,n):
        if n%x == 0:
            p = False
    return p

prime(17)
prime()
