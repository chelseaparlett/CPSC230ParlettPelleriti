def saleMaker(item, percent, inventory):
    inventory[item] = round(percent* inventory[item],2)
    percent = percent + 0.2 #get rid of stock
    # j = 1

i = {"apples": 2.45, "plumbs": 10.10, "almonds": 100.25}

nprice = .5
print("BEFORE:",i, nprice)
saleMaker("apples",nprice,i)
print("AFTER:",i,nprice)
#How can I change my code to automatically take 25% as the default price?
# How about the default item and dict are "apples" and {"apples": 10.5}

# Call saleMaker using all defaults, and with NO defaults.
# What if you just want to use the percent default?
#--------------------------------------------------
# Write a function prime, that has the default argument 100
# Call it using the default arguments, call it using 10
