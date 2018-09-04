# IF
x = 7
if x < 100:
    print("less than 100")
#--------------------------------
a = input("Type your favorite word ")

if a != "milquetoast":
    print("we don't have the same favorite word...")
#--------------------------------
if True:
    print("hello world")

#--------------------------------
# IF ELSE
num = 6

if num%10 == 0:
    print("divisible by 10")
else:
    print("not")
#--------------------------------
a = "a"

if a in 'aeiou':
    print("VOWEL!")
else:
    print("NOT a vowel.")
#--------------------------------
1 in 123

#in has to be used with collections
#--------------------------------
# WHILE
i = 0

while i < 10:
    print("I'm doing...something.")
    i += 1
#--------------------------------
while 10/2 == 5:
    print("Uh...")
#--------------------------------
x = 0
while x < 10 or x%2 ==1:
    print("... |", x)
    x += 1
else:
    print(x)
#--------------------------------
a = "the"

sentence = "the cat"

if a not in sentence:
    print("no the")
#--------------------------------
# SENTINEL LOOPS

k = True
j = "begin"

while k:
    if j == "horses":
        k = False
    else:
        j = input("pick a word.")
else:
    print("done")
#--------------------------------
j = "begin"

while True:
    if j == "horses":
        break
    else:
        j = input("pick a word.")
#--------------------------------
checker = 17

while checker < 1000:
    if checker%7 == 0:
        print(checker, "is divisible by 7")
        break
    checker += 1
#--------------------------------
f = 0

while f < 25:
    if f%2 == 0:
        f += 1
        continue
    else:
        f += 1
        print("odd")
#--------------------------------
