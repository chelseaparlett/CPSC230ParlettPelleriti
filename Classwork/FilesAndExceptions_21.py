# Class Activities + Review (Class 21)

# Together------------------------------------------------

# 0. Questions?
# 1. try/except
# 2. except with specific errors
# 3. raising errors
# 4. finally



'''
1. Write a function, story_reader(), which takes in an argument, f, which is a
filename/filepath to a text file containint a book/story. Use try and except
to account for the case when someone tries to give a value for f that does not
exist. If they give you a non-existant file, print out a message telling them,
and then open the file "boringStory.txt" instead (if you want to test this out
make sure you have the file "boringStory.txt" on your computer.)
'''

'''
2. Modify story_reader to account for both FileNotFound errors (when the file doesn't exist)
and an OSError when someone gives you a value for f that is not a filename (like an int).
Make sure to tell the user what their issue was.
'''

'''
3. Write a function, list_inserter() that takes in a list, l, an onject, x, and an index, i, as
arguments. The function should take x (which might be a string, an int...etc) and insert it into
the list l at index i.

Raise a ValueError if the index i is greater than len(l) (aka if they're trying to insert x into an
index that can't exist). Make sure you include a useful error message!
'''

'''
4. Write a function date_setter() that takes in current_month ("January"...etc) as
an argument. The function should then print out a message telling the user that they
MUST set an appointment with the dentist by the end of the year. Then it should ask
them which month they'd like to go to the dentist.

Raise a ValueError if they give you a month that's BEFORE the current month (e.g. if
current_month is June, they cannot say they want to go in March).

If they give you a valid month, ask them which day (1-31) they'd like to go. Raise
another ValueError if they give you a date that doesn't exist (e.g. February 30th).

If they give you a good date, print out a message confirming their appointment, and
return a string (e.g. "January 21") with their appointment date.
'''

'''
5. Write a function, banned_books(), which takes in a list of filenames (banned_list) containing books
that have been banned (like Farenheight 451, e.g.) as an argument. The function should ask
the user for the filename (as a string) of a book they'd like to read in class.

Raise a ValueError if the file they want is in the banned_list.

Call your function in a Try/Except block, and if a FileNotFound error occurs, print out a message
telling them their book doesnt exist, and ask them for another filename. If they put one of the banned books,
then yell at them, and tell them the book is bad. Then ask them for another filename.
'''
