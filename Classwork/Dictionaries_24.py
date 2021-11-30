# Class Activities + Review (Class 24)

# Together------------------------------------------------

# 0. Questions?
# 1. dicts are mutable like lists, what does that mean about changing it in a function?


'''
1. Using the Book dictionary below, write the following functions that do things
with the Book dictionary.

- update_read_perc() which takes in the book dictionary, and an integer, pages_read
as arguments. The function should calculate and update the percent_read.
- rate() which takes in the book dictionary, and a float (between 0 and 5), stars,
as arguments. The function should update the star_rating key/value.

Call these functions on Book.
'''
Book = {"title": "A Short History of Nearly Everything",
"author": "Bill Bryson",
"num_pages": 452,
"star_rating": 4.5,
"percent_read": 0}





'''
2. Using the dictionary below, write the following functions that do things with
the soccer_player dictionary.

- trade() which takes in the soccer player dictionary, and new_team (a string
representing the new team they'll be on) as arguments. Set the player's team
to be the new team and print a message welcoming them to the new team.
- goal() which takes in the player's dictionary and increments the player's goals
for the season by 1, and prints out "GOAAAAAAAAAAL".
- add_minutes() which takes in the player's dictionary and an int, mins, as arguments
and increments the player's minutes played by mins.
- end_game() which takes in the player's dictionary, an int, mins, and an int, goals,
as arguments and calls the goal() and add_minutes() functions for that game.
- bmi() which takes in the player's dictionary and returns their bmi.
- change_teams() which takes in the player's dictionary, their new team name as a string,
their player number (an int), and their new position (a string) as arguments. The function
should then change the dictionarie's team argument (using trade), update their jersey number,
and update their position. If their position and number are different from before, print
out a message telling them so.


Call all of these functions to test them out on the soccer_player dictionary.
'''
soccer_player = {"name": "Zlatan Ibrahimovic", "number": 11,
"team": "Galaxy", "height_cm": 195, "goals_season": 5,
"minutes_played_season": 466, "age": 40, "position": "FW",
"instagram": "@iamzlatanibrahimovic",
"weight_kg": 95}






'''
3. Using the Car dictionary below, write the following functions that do things
with the Car dictionary.

- calc_miles_left() which takes in the dictionary as an argument, and returns an
estimate of how many miles the car has left based on it's average mpg, and the
current number of gallons in the tank (tank_fill_current).
- calc_gas_cost() which takes in the dictionary, and a float, gas_price, which
is the cost of gas per gallon (e.g. 4.56) as arguments and returns the estimated
cost to fill up the tank *completely*.
- fill_tank() which takes in the dictionary, a float, gas_price, which
is the cost of gas per gallon (e.g. 4.56, and an int, num_gallons, as arguments
and prints out the cost to add num_gallons gallons of gas to the car, and then
changes tank_fill_current to reflect the refueling.
- drive() which takes in the dictionary, and a float, trip_miles, which tells you
how long the trip is in miles as arguments. The function should: use the average mpg
(mpg) to calculate how much gas will be used, and subtract it from tank_fill_current
(i know that's not exactly how cars work, but we're simplifying...). It should also
increase the odometer by the requisite number of miles.

'''
Car = {"make": "Honda",
"model": "Accord",
"year": 2006,
"mpg": 27,
"tank_vol_gallons": 15,
"tank_fill_current": 10,
"odometer": 79482.25}
