# list comp
# a = [[1,2,3,4,42,4,3,2],[4,2,3,9,5,83,8,2,9,0,3], [4,8,15,16,23,42]]
#
# newList = []
# for sub in a:
#     for i in sub:
#         newList.append(i)
# print(newList)
#
# newList2 = [i for sub in a for i in sub]
# print(newList2)

# b = [10,67,89,7,4,90,127,1024]
# c = [x*10 for x in b if x>10]
# print(c)
# c2 = []
# for x in b:
#     if x > 10:
#         c2.append(x*10)
# print(c2)
#
# def deckMaker(numDecks = 1):
#     suits = ["Hearts", "Spades", "Diamond", "Clubs"]
#     cards = ["A","K","Q","J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
#     deck = [(card + " of " + suit) for suit in suits for card in cards]
#     # for suit in suits:
#     #     for card in cards:
#     #         deck.append(card + " of " + suit)
#     return(deck * numDecks)
#
# def pwcheck(pw):
#     caps = False
#     symb = False
#
#     if pw != pw.lower():
#         caps = True
#     for sym in "!@#$%^&*()":
#         if sym in pw:
#             symb = True
#     if len(pw) >10 and caps and symb:
#         return(True)
#     else:
#         return(False)
#
# pwds = ["password123!", "thisISMYPASSWORD!", "yo", "1234567890!"]
#
# pwCheck = [pwcheck(pw) for pw in pwds]
# print(pwCheck)

def prime(n = 10):
    if n < 2:
        return(False)
    if n == 2:
        return(True)
    for div in range(2,n):
        if n%div == 0:
            return(False)
    return(True)

#primes between 3 and 700
primes = [i for i in range(3,701) if prime(i)]
print(primes)















# a = [[1,2,3,4,42,4,3,2],[4,2,3,9,5,83,8,2,9,0,3], [4,8,15,16,23,42]]
#
# b = []
# for sub in a:
#     for i in sub:
#         b.append(str(i))
# print(b)
# #make a list with all the values from these 3 lists using list comprehension
#
# b2 = [str(i) for sub in a for i in sub]
# print(b2)
#
#
# b = [10,67,89,7,4,90,127,1024]
# c = [x*10 for x in b if x>10]
#
# print(c)
#
# for x in b:
#     if x > 10:
#         c.append(x*10)
#
#
# #------
#
# def deckMaker(numdecks = 1):
#     suits = ["Hearts", "Spades", "Diamond", "Clubs"]
#     cards = ["A","K","Q","J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
#     deck = [(card + " of " + suit) for suit in suits for card in cards]
#     # for suit in suits:
#     #     for card in cards:
#     #         deck.append(card + " of " + suit)
#     return(deck*numdecks)
#
# #------
#
# #check a bunch of passwords, return a list of booleans about whether pws are good
#
# def pwcheck(pw):
#     Caps = False
#     symb = False
#
#     if pw != pw.lower():
#         Caps = True
#
#     for sym in "!@#$%^&*()":
#         if sym in pw:
#             symb = True
#
#     if len(pw) > 10 and Caps and symb:
#         return(True)
#     else:
#         return(False)
#
# pwds = ["password123!", "thisISMYPASSWORD!", "yo", "1234567890!"]
# pwBools = [pwcheck(p) for p in pwds]
# print(pwBools)
#
# #------
#
# def prime(n = 10):
#     if n < 2:
#         return(False)
#     if n == 2:
#         return(True)
#     for div in range(2,n):
#         if n%div == 0:
#             return(False)
#     return(True)
#
# print([i for i in range(0,100) if prime(i)])
