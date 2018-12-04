#Build a Tamagotchi class
class Tamagotchi():
    #init
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.love = 50
        self.hunger = 10
        self.thirst = 10
        self.tired = 0
        self.sleepy = False
        print("Hi! I'm your new Tamagotchi friend! My name is " + self.name)
    #feed
    def feed(self, numFood):
        self.hunger -= numFood*5
    #play
    def play(self, minutes):
        self.love += minutes *2
        self.tired += minutes *5
    #sleep
    def sleep(self,hours):
        self.tired -= 10*hours
        if self.tired < 0:
            self.tired = 0
    #check sleepy
    #kiss
    def kiss(self,otherT):
        self.love += 25
        otherT.love += 25
        print("MWHA!")

Blake = Tamagotchi("Blake","Blue")
print("Blake has:", Blake.tired, "tired")
Alex = Tamagotchi("Alex","Yellow")
print("Alex is " + Alex.color)

print("Blake Love: ", Blake.love)
print("Alex Love: ", Alex.love)

Blake.kiss(Alex)

print("post kiss Blake Love: ", Blake.love)
print("post kiss Alex Love: ", Alex.love)

#
