#1. Write a function, *SATscore()* which takes in as an argument a list of correct answers (answers can be "A", "B", "C", "D", or "E") and a list of the user's answers, and scores the test. Return a tuple of the raw score (how many they got right), and a percentage score (what percentage they got right). This function should work for any length lists, as long as they are the same length (make sure you check that in your function!)

# #YOUR CODE HERE
# def SATscore(corA,studentA):
#     studScore = 0
#     if len(corA) != len(studentA):
#         print("Your lists are not the same length")
#     for i in range(0,len(corA)):
#         if corA[i] == studentA[i]:
#             studScore += 1
#     return(studScore,studScore/len(studentA))
# print(SATscore(["A","B","A","C","B","C","C","A"],["C","B","A","C","C","C","C","A"]))


#2. Write a function, *anagramSolver()* that takes in a string as an argument, and returns a list of EVERY possible arrangement of the letters (you could use this to solve anagrams because you could look through all the arrangements and see which one is a real word!). For example, if the argument string was "cat", this function should return ["cat","cta", "tac", "tca", "act", "act"]. This needs to work for any string with 3 characters. Try to do this without hardcoding each of the 6 possible answers, think loops.

# #YOUR CODE HERE
# def anagramSolver(st):
#     arrangs = []
#     for i in range(0,3):
#         a = [0,1,2]
#         a.remove(i)
#         for k in a:
#             a.remove(k)
#             j = a[0]
#             arrangs.append(st[i] + st[k] + st[j])
#             arrangs.append(st[i] + st[j] + st[k])
#     return(arrangs)
# print(anagramSolver("dog"))

#3. Write a function, *grade_calc()* which takes in a dictionary something like this: {"exams": {"grade": 90, "weight": 40},"quizzes": {"grade": 85, "weight": 20},"homework": {"grade": 85, "weight": 40}} (although it should work if there is a different number of categories.). First, check if the weights add up to 100%, if they do not, print a warning message and return 0. Otherwise, use the weights and the grades to calculate the overall grade in the course and return it. (In the dictionary example I gave, the final grade would be an 87%)

# #YOUR CODE HERE
# def grade_calc(d):
#     perc_sum = 0
#     for item in d:
#         perc_sum += d[item]["weight"]
#     if perc_sum != 100:
#         print("Weights not Correct")
#         return(0)
#     grade = 0
#     for item in d:
#         grade += d[item]["grade"] * (d[item]["weight"]/100)
#     return(grade)
# print(grade_calc({"exams": {"grade": 90, "weight": 40},"quizzes": {"grade": 85, "weight": 20},"homework": {"grade": 85, "weight": 40}}))


#4. (WARNING: this is very difficult, the test wont be this hard, but this is good practice!) Write a function, *battleship()* which runs a very simple game of battle ship. It takes in two arguments, a list of lists for User1, and a list of lists for User2 (see below for example). 1's represent a space where there is a ship, O's represent somewhere where there is NOT a ship. Run a game of battle ship in which each user alternates guessing the row (0-5) and column (0-5) where they think the opponent's ship is. Check the opponent's grid, and print a statement telling the user whether they hit a ship or not (remember, a ship will have a 1). Then print out a grid for the user to show which places they've guessed and whether it's been a hit or a miss. Once all of an opponent's ships have been found, the game is over. Print ("GAME OVER"). Feel free to write other necessary functions to run this game.
#YOUR CODE HERE
def notwon(g,u):
    win = False
    for r in range(0,5):
        for c in range(0,5):
            if u[r][c] == 1 and g[r][c] != 1:
                win = True
    return(win)
    print(win)
    return(win)
def guessGrid(guesses,opponent):
    guessG = blankGrid()
    for r in range(0,5):#each row
        for c in range(0,5):#each item in row
            if guesses[r][c] != 0:
                if opponent[r][c] == 1:
                    guessG[r][c] = "H"
                else:
                    guessG[r][c] = "M"
    return(guessG)
def blankGrid():
    return([[0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]])
def showGrid(grid):
    print("  0 1 2 3 4")
    for r in range(0,5):
        st = str(r) + "|"
        for i in grid[r]:
            st += str(i) + " "
        print(st)
def battleship(Use1, Use2):
    print("\nWELCOME TO BATTLE SHIP. PLAYER1 here is your grid: ")
    showGrid(Use1)
    print("\n PLAYER2 here is your grid: ")
    showGrid(Use2)
    print("ALRIGHT LET'S PLAY!")
    U1Guesses = blankGrid()
    U2Guesses = blankGrid()
    while notwon(U1Guesses,Use2) and notwon(U2Guesses,Use1):
        print("\nplayer1---------------------")
        print("SO FAR YOU'VE GUESSED:")
        GG1 = guessGrid(U1Guesses,Use2)
        showGrid(GG1)
        r = int(input("PLAYER 1, which row?"))
        c = int(input("PLAYER 1, which column?"))
        while r not in [0,1,2,3,4] or c  not in [0,1,2,3,4]:
            r = int(input("PLAYER 1, which row?"))
            c = int(input("PLAYER 1, which column?"))
        U1Guesses[r][c] = 1
        if Use2[r][c] == 1:
            print("\nHIT!")
        else:
            print("\nMISS!")
        if notwon(U1Guesses,Use2):
            print("\nplayer2---------------------")
            print("SO FAR YOU'VE GUESSED:")
            GG2 = guessGrid(U2Guesses,Use1)
            showGrid(GG2)
            r = int(input("PLAYER 2, which row?"))
            c = int(input("PLAYER 2, which column?"))
            while r not in [0,1,2,3,4] or c  not in [0,1,2,3,4]:
                r = int(input("PLAYER 2, which row?"))
                c = int(input("PLAYER 2, which column?"))
            U2Guesses[r][c] = 1
            if Use1[r][c] == 1:
                print("HIT!")
            else:
                print("MISS!")
    else:
        print("GAME OVER")
        if notwon(U1Guesses,Use2):
            print("PLAYER 2 won")
        else:
            print("PLAYER 1 won")



U1 = [[1,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]
U2 = [[1,1,1,0,0],
      [0,0,0,0,0],
      [0,1,1,1,1],
      [0,0,0,0,1],
      [0,0,0,0,1]]
battleship(U2,U1)
