# Class Activities + Review (Class 4)

# Together------------------------------------------------

# 0. Questions?
# 1. Comparison Operators
# 2. Int Operators
    # a. Modulo
    # b. Floor Division
# 3. Precedence/OOO

10 + 2 ** 3 - (4+5) + 49/7 * 2

# What's the Answer? BONUS: will this be a float or int?
# What Order should we go in?
# how could we write this BETTER?


# Frasier Episodes (https://en.wikipedia.org/wiki/List_of_Frasier_episodes)
# Frasier had 264 wonderful episodes, 24 per season for 11 seasons. 
# When I scraped the Frasier Script data, the files were numbered
# by overall episode number (e.g. 1-264), not in Season-Episode
# form (e.g. Season 1, Episode 13). 
# Use Operators (hint: //, %) to write some code that will take an
# overall episode number (e.g. 1-264) stored in the variable frasier,
# and print out the Season and Episode Number (e.g. Season 1, Episode 13).
# (this is a problem I actually had to solve IRL!)
# HINT: would it be easier if we pretended that seasons/episode started
# counting at 0 and then just added 1 after? E.g. what if the seasons
# were numbered 0-10, and episodes 0-23? Would that be easier?

ep_num = 25

season = ???
episode = ???

print(...)
# Classwork-----------------------------------------------
'''
1. Without using Python, figure out the answer to this statement:

    4 * 2 * 4 + 6 ** 8 // 2 + 6 - 7 * 9 + (16 + 4)

2. Check your answer using Python.'''

# code

'''
3. Rewrite this equation using more parentheses to make it a little
bit clearer what order things are run in.
'''

# 4 * 2 * 4 + 6 ** 8 // 2 + 6 - 7 * 9 + (16 + 4)

'''
4. Using Comparison Operators, make a complicated statement (use at
 least 5 operators, repeats allowed) that evaluates to False.
'''

'''
5. Using Comparison Operators, make a complicated statement (use at
 least 5 operators, repeats allowed) that evaluates to True.

'''
'''
6. What happens when you turn True into an int? False?
'''

'''
7. Using modulo, check whether 1069 is even.
'''

'''
8. Using your operators (%,/,//,*), write some code to convert an amount of
time in minutes (e.g. 257) to hours and minutes (e.g. 4 hours and 17 minutes).
Print out the numbers of hours/minutes in the form "X hours, Y minutes".
Try it with multiple values:
- 12,938 (answer: 215 hours, 38 minutes)
- 55 (answer: 0 hours, 55 minutes)
- 525,600 (answer: 8760 hours, 0 minutes )
- 432 (answer: 7 hours, 12 minutes)
'''

m = 12938

# your code here

'''
9. Extend the code above to print out days (assume 24 hours per day), and
Weeks (7 days per week). Again, print out the minutes, hours, days, weeks
in the form "A weeks, B days, X hours, Y minutes".
Try it with multiple values:
- 525,600 (answer: 52 weeks, 0 days, 0 hours, 0 minutes)
- 1,000,000 (answer: 99 weeks, 1 days, 10 hours, 40 minutes)
'''

'''
10. Write some code that uses two separate input functions to ask
the user for the time of day in military (24 hour time)
by asking FIRST for the hour, then SECOND asking for the minutes.
E.g. for the time 13:25 the user should enter 13 for the first input
statement, and 25 for the second.
Use your operators to convert from military time to AM/PM time
(e.g. 13:25 should be converted to 1:25).
'''