# Extra File Practice---------------------------------------------------------
# Write a function clubPenguin() that takes in the name of a file, message, as
# an argument. It should also take in a string, name, that has the user's name.
# Your function should create a new string that has their name, then a colon (:)
# and then the message for each line in the file. However the message should not contain the words "gosh",
# "darn", or "shoot". If those strings are in the message, you should replace
# them with asterisks (one asterisk per letter in the replaced word). Write this
# new message to the file "CP.txt".
# YOUR CODE HERE -------------------------------------------------------------
def clubPenguin(name, message = "hi.txt"):
    message = open(message,"r")
    whole_message = ""
    for line in message:
        whole_message += name
        whole_message += ": "
        whole_message += line
    print(whole_message)
    words = ["gosh", "darn", "shoot"]
    message.close()

    for word in words:
        if word in whole_message.lower():
            whole_message = whole_message.replace(word, ('*'*len(word)))

    w = open("CP.txt","w")
    w.write(whole_message)
    w.close()

clubPenguin("Chelsea", "hi.txt")

#/YOUR CODE HERE -------------------------------------------------------------

# Write a function called RickRoll() that takes in a filename, fn, as an argument.
# Open the file, and add the first few lines of the song Never Gonna Give you Up
# by Rick Astley to the file. Return a message that tells them they've been Rick
# Rolled.
# YOUR CODE HERE -------------------------------------------------------------

def RickRoll(fn):
    f = open(fn, "a")
    f.write("Never gonna give you up\nNever gonna let you down")
    f.close()
    return("You've be Rick Rolled!")
#/YOUR CODE HERE -------------------------------------------------------------
