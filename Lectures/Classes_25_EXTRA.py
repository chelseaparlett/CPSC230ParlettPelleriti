# die
import random

class Die():

    def __init__(self, sides = 6):
        self.num_sides = sides
        self.roll_history = []
        print("Die Created")

    def add_roll(self, r):
        self.roll_history.append(r)

    def roll(self):
        r = random.randint(1, self.num_sides)
        print("You rolled a " + str(r))

        self.add_roll(r)

        return(r)

    def roll_mult(self, n):
        r = [self.roll() for i in range(0,n)]

        return(r)

glenn = Die(20)

# x = glenn.roll()
# print(x)

coin = Die(2)

coin.roll_mult(5)

coin.roll()

print(coin.roll_history)
