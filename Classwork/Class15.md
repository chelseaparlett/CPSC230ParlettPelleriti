# Harry Potter Battle!
<p>We're at Hogwarts and it's time to practice spells! Using Dictionaries for the characters Harry, and Hermione, that store their Hogwarts House, Health points, number of successful spells, and a list of spells cast, write a script that rotates between all 4 characters. Randomly select a spell to cast from the dictionary, spells_dict [HINT: random.choice(spells_dict.keys()). Use the one we made in class before]. </p>

<p> There are 5 Rounds. For each round, both Harry and Hermione attempt to cast a spell. Harry only has a 50% chance of getting the spell correct. Hermione has a 75% chance of getting a spell correct (HINT: random.choice(["hit","miss"]) has a 50% chance of choosing hit and miss.) </p>

<p> If the spell is successful, store the spell name in the player's dictionary, subtract the damage done from the opponent's health (stored in their dictionary), print "Success, [name of character]!" and add one to their successful spells count. IF it is not successful, just print "Better Luck Next Time, [character]." </p>
