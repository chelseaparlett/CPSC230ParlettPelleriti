# Write a function order() which takes in 1 argument:
#a string representing the item the customer wishes to
#purchase. Inside the function, ask the user how many they
#want to buy.
#Use try/except to make sure that the number they want is
#a number. Print out a string
#telling the customer what they ordered and how many.
def order(item):
    n = input("how many do you want? ")
    while True:
        try:
            n = int(n)
            break
        except:
            print("that's not a number")
            n = input("how many do you want? ")
    print("You are buying",n,item,"s")

#Ask the user which file they want to read from. Using try/except
#make sure the file exists. Then print each line of the file,

f = input("file name: ")
while True:
    try:
        fn = open(f,"r")
        break
    except:
        print("not a file")
        f = input("file name: ")

#Modify your quadratic assignment to use try/except to catch
#when you're trying to take the squareroot of negative numbersself.
import math
a = input("enter coef: ")
b = input("enter coef: ")
c = input("enter coef: ")

d = b**2 - 4*a*c

try:
    d = math.sqrt(d)
    print("ROOTS ARE:")
    print((-b + d)/(2*a))
    print((-b - d)/(2*a))
except:
    print("THOSE numbers don't work.")

#or

import math
a = input("enter coef: ")
b = input("enter coef: ")
c = input("enter coef: ")

d = b**2 - 4*a*c
while True:
    try:
        d = math.sqrt(d)
        break
    except:
        print("THOSE numbers don't work.")
        a = input("enter coef: ")
        b = input("enter coef: ")
        c = input("enter coef: ")
        d = b**2 - 4*a*c
print("ROOTS ARE:")
print((-b + d)/(2*a))
print((-b - d)/(2*a))
