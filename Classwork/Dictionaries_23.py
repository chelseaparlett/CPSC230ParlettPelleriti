# Class Activities + Review (Class 23)

# Together------------------------------------------------

# 0. Questions?
# 1. in
# 2. loops
# 3. sets
# 4.

# in in dicts

d = {"name": "Igui" , "GDP (in millions)": 26656766, "unemployment rate": 4.88,
"number of flu cases (2020)": 189234, "population": 1439323776,
"socialized healthcare": True, "national language": "English",
"life expectancy": 78.6, "CO2 emissions (in tons)": 15.12}



# sets
 great_britain = {"Scotland", "England", "Wales"}
 uk_of_gb_and_northern_ireland = {"Scotland", "England", "Wales", "Northern Ireland"}
 ireland = {"Northern Ireland", "Republic of Ireland"}
 british_isles = {"Scotland", "England", "Wales", "Northern Ireland",
  "Republic of Ireland", "Isle of Man"}


## union


## difference


## intersection

## symmetric difference


'''
1. Write a function shopping_list_helper() that takes in a list of lists, recipes,
as an argument. The sublists contain ingredients for a recipe (see below). Using
sets, print out a list of unique ingredients needed by all of the recipes.
'''

my_recipes = [["apples", "sugar", "cinnamon", "nutmeg", "cloves", "butter", "flour", "vodka"],
["ground beef", "refried beans", "lettuce", "cheese", "tomato", "sour cream", "avocado"],
["lettuce", "croutons", "parmesean", "anchovies", "mayo", "mustard", "worcestershire", "lemon"],
["lemon", "sugar", "flour", "vanilla", "butter", "eggs"],
["eggs", "tomato", "bacon", "blue cheese", "lettuce", "cheese", "cucumber"]]




'''
2. Using the three list below, figure out which shows/movies are

- only on netflix and no other platform
- only on hulu and no other platform
- on both netflix and hulu
- are on netflix, hulu, and amazon_prime
- are unique to their platform (e.g. shows/movies that only appear on one platform)

'''
netflix = ["Seinfeld", "The Great British Baking Show", "The Good Place", "Greys Anatomy", "Friends",
"You", "Arrested Development", "The Witcher", "Riverdale", "Uncut Gems", "The Lorax", "Breaking Bad", "The Office"]
hulu = ["Seinfeld", "Greys Anatomy", "Friends", "The Good Doctor", "The Office", "Bob's Burgers", "Cougar Town", "The Simpsons",
"Superstore", "It's Always Sunny in Philidelphia", "Desperate Housewives", "Futurama", "Frasier", "Shrek", "Parasite"]
amazon_prime = ["Seinfeld", "Spongebob", "Dexter", "Midsommar", "The Princess Bride", "Cast Away", "The Tomorrow War", "House MD", "Fight Club",
"Mrs. Doubtfire", "The Office", "The Simpsons", "Friends"]



'''
3. Create a function, stencil_finder(), that takes in a message as a string as an argument.
The function is to help a graffiti artist know which stencils they have to bring with them
to tag a message in their city. Since stencils for graffiti can be reused, they only need
to know which to take, not how many. The functions should take the message, figure out which
letter stencils are needed, and print and return a list of them for the artist.

'''




'''
4. Our graffiti artist is going to graffiti multiple messages in one night.
Modify stencil_finder() so that it takes in a list of messages instead of one message,
and still prints and returns a list of letters/stencils needed to tag ALL the messages.
'''




'''
5. The list of dictionaries below contains information about different (fake) countries,
but not all the country dictionaries have the same keys!

Loop through the dictionaries and using the in operator, find:
- the mean GDP for all countries
- the # of flu cases per capita (per person)
- the average unemployment rate for countries with and without national/socialized healthcare.

If a country does not have the pertinent key, do not include it in the above
calculations.
'''
countries = [
{"name": "Igui" , "GDP (in millions)": 26656766, "unemployment rate": 4.88,
"number of flu cases (2020)": 189234, "population": 1439323776,
"socialized healthcare": True, "national language": "English",
"life expectancy": 78.6, "CO2 emissions (in tons)": 15.12},

{"name": "Central Ini" , "GDP (in millions)": 3231927, "unemployment rate": 5.27,
"population": 206139589,
"socialized healthcare": True, "national language": "Nereti",
"life expectancy": 75.09, "CO2 emissions (in tons)": 12.65},

{"name": "Buslandsri" , "GDP (in millions)": 2613797, "unemployment rate": 5.33,
"number of flu cases (2020)": 112389, "population": 212559417,
"socialized healthcare": True, "national language": "Kuunarin",
"life expectancy": 74.54, "CO2 emissions (in tons)": 10.49},

{"name":"Southern Taphi" , "GDP (in millions)": 1705519,
"number of flu cases (2020)": 169509, "population": 	97338579,
"socialized healthcare": False, "national language": "English",
"life expectancy": 80.15, "CO2 emissions (in tons)": 9.02},

{"name": "Rdanslands Tani" , "GDP (in millions)": 1346225, "unemployment rate": 7.62,
"number of flu cases (2020)": 126832, "population": 59308690,
"socialized healthcare": False, "national language": "Oldian",
"life expectancy": 79.81, "CO2 emissions (in tons)": 11.15},

{"name": "Theri" , "unemployment rate": 2.22,
"number of flu cases (2020)": 111975,
"socialized healthcare": True, "national language": "English",
"life expectancy": 77.66, "CO2 emissions (in tons)": 11.09},

{"name": "Marniaxi", "GDP (in millions)": 3231927, "unemployment rate": 2.03,
"number of flu cases (2020)": 219020, "population": 83783942,
"socialized healthcare": False, "national language": "Kuunarin",
"life expectancy": 79.24, "CO2 emissions (in tons)": 16.13},

{"name":0 , "GDP (in millions)": 1363766,
"number of flu cases (2020)": 102875, "population": 	89561403,
"socialized healthcare": True, "national language": "Oldian",
"life expectancy": 78.12, "CO2 emissions (in tons)": 15.81},

{"name":"Republic of Stanzacai" , "GDP (in millions)": 1148580, "unemployment rate": 5.98,
"number of flu cases (2020)": 104847, "population": 331002651,
"socialized healthcare": False, "national language": "Aafuznesh",
"life expectancy": 77.61, "CO2 emissions (in tons)": 9.56},

{"name": "Govo Cari" , "GDP (in millions)": 1000617, "unemployment rate": 4.31
,
"number of flu cases (2020)": 159028, "population": 273523615,
"socialized healthcare": True, "national language": "English",
"life expectancy": 73.24, "CO2 emissions (in tons)": 13.7},

{"name": "Felandti", "GDP (in millions)": 966485, "unemployment rate": 4.88,
"number of flu cases (2020)": 99287, "population": 34813871,
"socialized healthcare": True, "national language": "Aafuznesh",
"life expectancy": 83.41, "CO2 emissions (in tons)": 7.81}
]


'''
6. Write a function consider_food() that takes in 2 arguments: food, a dictionary with
the different allergen/ingredient booleans (see sandwhich and apple below), and
allergies, a list of keys (as strings) indicating which allergens/foods this person
cannot consume. (e.g. if the list is ["gluten", "dairy"] then that person cannot
eat anything with gluten or dairy.)

The function should check whether the food is something the person can eat. If it is
return True, else return False.
'''

sandwhich = {"name": "sandwhich","gluten": True, "meat": True, "Soy": True, "AnimalProducts": True}
apple = {"name":"apple","gluten": False, "meat": False, "Soy": False, "AnimalProducts": False}
cheese = {"name":"cheese","gluten": False, "meat": False, "Soy": False, "AnimalProducts": True}
tofu = {"name":"tofu","gluten": False, "meat": False, "Soy": True, "AnimalProducts": False}


'''
Finish any problems from the last Dictionaries classwork
'''
