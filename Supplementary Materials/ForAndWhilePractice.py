#1-----------------------------------------------------
# Use a loop to count the numer of question marks in the
# following string:

s = '''According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway. Because bees don’t care what humans think is impossible.” SEQ. 75 - “INTRO TO BARRY” INT. BENSON HOUSE - DAY ANGLE ON: Sneakers on the ground. Camera PANS UP to reveal BARRY BENSON’S BEDROOM ANGLE ON: Barry’s hand flipping through different sweaters in his closet. BARRY Yellow black, yellow black, yellow black, yellow black, yellow black, yellow black...oohh, black and yellow... ANGLE ON: Barry wearing the sweater he picked, looking in the mirror. BARRY (CONT’D) Yeah, let’s shake it up a little. He picks the black and yellow one. He then goes to the sink, takes the top off a CONTAINER OF HONEY, and puts some honey into his hair. He squirts some in his mouth and gargles. Then he takes the lid off the bottle, and rolls some on like deodorant. CUT TO: INT. BENSON HOUSE KITCHEN - CONTINUOUS Barry’s mother, JANET BENSON, yells up at Barry. JANET BENSON Barry, breakfast is ready! CUT TO: "Bee Movie" - JS REVISIONS 8/13/07 1. INT. BARRY’S ROOM - CONTINUOUS BARRY Coming! SFX: Phone RINGING. Barry’s antennae vibrate as they RING like a phone. Barry’s hands are wet. He looks around for a towel. BARRY (CONT’D) Hang on a second! He wipes his hands on his sweater, and pulls his antennae down to his ear and mouth. BARRY (CONT'D) Hello? His best friend, ADAM FLAYMAN, is on the other end. ADAM Barry? BARRY Adam? ADAM Can you believe this is happening? BARRY Can’t believe it. I’ll pick you up. Barry sticks his stinger in a sharpener. SFX: BUZZING AS HIS STINGER IS SHARPENED. He tests the sharpness with his finger. SFX: Bing. BARRY (CONT’D) Looking sharp. ANGLE ON: Barry hovering down the hall, sliding down the staircase bannister. Barry’s mother, JANET BENSON, is in the kitchen. JANET BENSON Barry, why don’t you use the stairs? Your father paid good money for those. "Bee Movie" - JS REVISIONS 8/13/07 2. BARRY Sorry, I’m excited. Barry’s father, MARTIN BENSON, ENTERS. He’s reading a NEWSPAPER with the HEADLINE, “Queen gives birth to thousandtuplets: Resting Comfortably.” MARTIN BENSON Here’s the graduate. We’re very proud of you, Son. And a perfect report card, all B’s. JANET BENSON (mushing Barry’s hair) Very proud. BARRY Ma! I’ve got a thing going here. Barry re-adjusts his hair, starts to leave. JANET BENSON You’ve got some lint on your fuzz. She picks it off. BARRY Ow, that’s me! MARTIN BENSON Wave to us. We’ll be in row 118,000. Barry zips off. BARRY Bye! JANET BENSON Barry, I told you, stop flying in the house! CUT TO: SEQ. 750 - DRIVING TO GRADUATION EXT. BEE SUBURB - MORNING A GARAGE DOOR OPENS. Barry drives out in his CAR. "Bee Movie" - JS REVISIONS 8/13/07 3. ANGLE ON: Barry’s friend, ADAM FLAYMAN, standing by the curb. He’s reading a NEWSPAPER with the HEADLINE: “Frisbee Hits Hive: Internet Down. Bee-stander: “I heard a sound, and next thing I knew...wham-o!.” Barry drives up, stops in front of Adam. Adam jumps in. BARRY Hey, Adam. ADAM Hey, Barry. (pointing at Barry’s hair) Is that fuzz gel? '''
# YOUR CODE HERE---------------------------------------------
# qmCount = 0
# for char in s:
#     if char == "?":
#         qmCount += 1
# print("there are " + str(qmCount) + " question marks.")

# END YOUR CODE HERE-----------------------------------------

#2-----------------------------------------------------------
# Write a loop that checks if user generated input matches
# their password, which is stored in the variable pw. Continue
# asking them for their password until they get it correct.
# then print a message saying their login was successful.

pw = "Password1"

# YOUR CODE HERE---------------------------------------------
# guess = input("please enter your password: ")
#
# while guess != pw:
#     guess = input("please enter your password: ")
# else:
#     print("Logged in")

# END YOUR CODE HERE-----------------------------------------

#3-----------------------------------------------------------
# Write a loop that does the same thing as the code above
# but also limits users to 10 incorrectnguesses before it
# prints out a message saying "You've been blocked".

pw = "Password1"

# YOUR CODE HERE---------------------------------------------
# guess = input("please enter your password: ")
# num_guess = 1
#
# while guess != pw and num_guess < 10:
#     guess = input("please enter your password: ")
#     num_guess += 1
# else:
#     if num_guess < 10:
#         print("Logged in")
#     else:
#         print("You've been blocked")

# END YOUR CODE HERE-----------------------------------------

#4-----------------------------------------------------------
# Write a loop that checks every number from 0 to 100 to see
# if that number is even. if it is, print "EVEN"

# YOUR CODE HERE---------------------------------------------

for n in range(0,101):
    if n%2 == 0:
        print("EVEN")


# END YOUR CODE HERE-----------------------------------------
