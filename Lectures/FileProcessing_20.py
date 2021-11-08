# reading files

# create a connection with this document
g = open("gettysberg.txt", "r")

# loop through the lines and print them
for line in g:
    print(line)

# close our connection to the file
g.close()


# 404
g2 = open("gettysberg2.txt", "r")




# writing files

# create a connection with this document (overwrite if it exists)
poem = open("my_poem.txt", "w")

# write lines to doc
poem.write("'You are old, Father William' the young man said.\n")
poem.write("'And your hair has become very white;\n")
poem.write("And yet you incessantly stand on your head\n")
poem.write("Do you think, at your age, it is right?'\n")

# close our connection to the file
poem.close()

## what happens if this file already exists?





# appending files
# poem = open("my_poem.txt", "w")
poem = open("my_poem.txt", "a")

# write lines to doc
poem.write("\n")
poem.write("'In my youth,' Father William replied to his son,\n")
poem.write("I feared it might injure the brain;\n")
poem.write("But now that I'm perfectly sure I have none,\n")
poem.write("Why, I do it again and again.'\n")

# close our connection to the file
poem.close()




# reading and writing files
input = open("input.txt", "r")
output = open("output.txt", "w")

i = 1
for line in input:
    new_str = str(i) + " " + line + "\n"
    output.write(new_str)
    i += 1

input.close()
output.close()


'''Open a  file to read (“my_file.txt”)
Read through the file
Clean the file (get rid of spaces, make it lowercase)
Find words that have ALL the vowels (aeio AND u) and store them in a list.
Assume no punctuation is in the file'''

all_the_vowels = []

with open("my_file.txt", "r") as f:
    for line in f:
        line = line.split()
        for word in line:
            if "a" in word.lower() and "e" in word.lower() and "i" in word.lower() and "o" in word.lower() and "u" in word.lower():
                all_the_vowels.append(word)
print(all_the_vowels)

# csv

import csv

csv_file_path = "/Users/chelseaparlett/Desktop/Desktop/School/CPSC230ParlettPelleriti/ResourcesAndData/cereal.csv"

f = open(csv_file_path, "r")

csv_object = csv.reader(f, delimiter = ",")

csv_lists = []

for row in csv_object:
    csv_lists.append(row)
    # print(row)


cals = csv_lists[0].index("calories")
print(cals)

calories = []

for row in csv_lists:
    if row[0] == "name":
        continue
    calories.append(float(row[cals]))

print(sum(calories)/len(calories))
