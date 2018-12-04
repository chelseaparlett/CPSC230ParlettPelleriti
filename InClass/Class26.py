#Build a Tamagotchi class
class Tamagotchi():
    #init
    #feed
    #play
    #sleep
    #check sleepy
    #kiss

Blake = Tamagotchi("Blake","Blue")
print("Blake has:", Blake.tired, "tired")
Alex = Tamagotchi("Alex","Yellow")
print("Alex is " + Alex.color)

print("Blake Love: ", Blake.love)
print("Alex Love: ", Alex.love)

Blake.kiss(Alex)

print("post kiss Blake Love: ", Blake.love)
print("post kiss Alex Love: ", Alex.love)

Alex.checkSleep()
