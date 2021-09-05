# if

x = 0

if x > 5:
    x += 1
print("done")



name = "Chelsea"
if name == "Chelsea":
    print("You're the professor.")

# if/else

answer = int(input("What is 4 * 6"))

if answer == 24:
    print("Correct")
else:
    print("Ooof.")

answer2 = input("African or European Swallow?")

if answer2 == "African":
    print("ah!")
else:
    print("no.")

print("Swallows are a migratory species.")

# Basketball

points = int(input())
points = points - 3

lead = input("Who has the ball? The leading team or the other team? ")

if lead == "other team":
    points -= 0.5
if lead == "leading team":
    points += 0.5

if points < 0:
    points = 0

seconds = int(input("How many seconds are left in the game? "))

if points > seconds:
    print("SAFE")
else:
    print("NOT SAFE")
