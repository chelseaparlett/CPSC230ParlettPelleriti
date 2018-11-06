# FILE I/O and Functions
import csv

reader = csv.DictReader(open("heroes_information.csv", 'r'))

# for row in reader:
#     print(list(row.keys()))
#     print(dict(row))
#     break
#--------------------------------
# i = 0
# for row in reader:
#     i += 1
#     print(row["name"] + " is a " + row["Gender"] + " " + row["Race"])
#     if i >20:
#         break
#--------------------------------
# pub = {}
# for row in reader:
#     if row["Publisher"] in pub:
#         pub[row["Publisher"]] += 1
#     else:
#         pub[row["Publisher"]] = 1
# print(pub)
#--------------------------------
def blueChecker(dictionary):
    if dictionary["Skin color"].lower() == "blue":
        print("OH CRAP THEY'RE BLUE!")
        return True
    else:
        return False
i = 0
blues = []
for row in reader:
    i += 1
    b = blueChecker(row)
    blues.append(b)
    if i > 300:
        print(sum(blues))
        break
