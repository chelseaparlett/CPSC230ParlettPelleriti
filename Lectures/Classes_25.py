# CLASSES


# square
class Square():
    shape = "square"
    side_count = 4

    def __init__(self, side):
        self.side_length = side
        print("Hello There! I am a Square. It's good to be alive.")

    def area(self):
        return(self.side_length ** 2)

    def perimeter(self):
        return(self.side_count * self.side_length)

    def scaleSize(self, scaler):
        self.side_length *= scaler


bob = Square(4)
print(bob.side_length)
print(bob.shape)

a = bob.area()
p = bob.perimeter()
print(p)

bob.scaleSize(2)
print(bob.side_length)


# Turn student dictionary example into a class
'''
Create a dictionary called student. It should have the keys: name, age, major, minor,
year, classes_current, classes_all, and clear_status.

Write the following functions:
-- rename() which takes in the dictionary, and a variable, new_name. Replace their
current name with new_name.
-- end_semester() which takes in the dictionary, and which moves all their current
classes to their list of ALL classes, and empties current classes.
-- major_declare() which takes in their dictionary, and a string, major, and
updates their major.
-- minor_declare() which does the same thing, but for minor.
-- covid_clear() which takes in the dictionary, and a boolean, survey, which
indicates whether or not the student has said "no" to all the covid screening
questions on their daily survey. It then changes their status to "CLEAR" or
"NOT CLEAR" based on the survey.
'''

class Student():

    def __init__(self, name, age, major, minor, classes_current):
        self.name = name
        self.major = major
        self.minor = minor
        self.age = age
        self.classes_current = classes_current
        self.classes_all = []
        self.clear_status = "NOT CLEAR"
        print("Welcome to Chapman " + self.name)

    def rename(self, new_name):
        self.name = new_name
        print("We've updated your records to reflect your new name!")

    def end_semester(self):
        self.classes_all += self.classes_current
        self.classes_current = []
        print("Great job this semester!")

    def major_declare(self, major):
        self.major = major
        print("Your major is now: " + major)

    def minor_declare(self, minor):
        self.minor = minor
        print("Your minor is now: " + minor)

    def covid_clear(self, survey):
        if survey:
            self.clear_status = "CLEAR"
        else:
            self.clear_status = "NOT CLEAR"
        print("Thats for filling out your survey.")


john = Student("John", 21, "Electrical Engineering", "Data Analytics", ["CPSC230"])
print(john.name)
print(john.major)

john.covid_clear(survey = False)
print(john.clear_status)
