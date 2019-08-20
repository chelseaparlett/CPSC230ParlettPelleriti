#Try and Except---------------------------------
# Chapter 6.6
#
# print("NO ERROR HANDLING-------------------------")
# fn = int(input("what's your favorite number? "))
#
# #what could go wrong?
# #
# print("WHILE LOOP--------------------------------")
fn = input("what's your favorite number? ")
while not fn.isnumeric():
    fn = input("what's your favorite number? ")
fn = int(fn)
#
# # #how have we fixed it in the past?
# #
# #try/Except
# print("TRY EXCEPT #1--------------------------------")
# try:
#     fn = int(input("what's your favorite number? "))
# except:
#     print("That's not a number, I'll pretend you said 7.")
#     fn = 7
#
# # #or
# print("TRY EXCEPT #2--------------------------------")
# while True:
#     try:
#         fn = int(input("what's your favorite number? "))
#         break
#     except:
#         print("That's not a number")

#
# print("\n\nFILE ISSUES-----------------------------------")
#reader = open("Chelsea.txt", "r")
# #what can go wrong?
#
# try:
#     filename = input("filename: ")
#     reader = open(filename, "r")
# except:
#     print("YOU MESSED UP. GO CHECK YOUR FILE LOCATION.")

# while True:
#     try:
#         filename = input("filename: ")
#         reader = open(filename, "r")
#         break
#     except:
#         print("YOU MESSED UP. GO CHECK YOUR FILE LOCATION.")

#
#
#List Comprehension
# Chapter 7.11
# a = ["A","B","C","D","E"]
#
# b = []
# for i in a:
#     b.append(i.lower())
# print(b)
#
# b2 = [i.lower() for i in a]
# print(b2)
# b2 = [i.lower() for i in a]
# print(b2)
#
c = ["The quick brown fox A", "Mary had a little lamb", "New in Town"]
vows = []
for s in c:
    for letter in s:
        if letter.lower() in "aeiou":
            vows.append(letter)

print(vows)
vows2 = [letter for s in c for letter in s if letter.lower() in "aeiou"]
print(vows2)






# vows2= [letter for s in c for letter in s if letter.lower() in "aeiou"]
# print(vows2)
#
#
#Classes
# Chapter 11 (all)
class Cat:
    def __init__(self,name):
        self.name = name
        print("MEOW, I'm ", self.name)
    def meow(self):
        print(self.name + ": MEOW!")
Blake = Cat("Blake")
John = Cat("John")
Blake.meow()
#Functions
# Chapters 5 and 8
