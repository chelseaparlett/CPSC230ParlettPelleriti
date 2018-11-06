* Write a function fact() that takes a number n as an argument and returns the factorial of that number and prints out "YOUR ANSWER IS #!" (replace # with the answer). Set the default argument for n to 10.
* Write a function called youTube() that takes in name (the name of the channel), action (like, subscribe, or notification), and a dictionary, creators. Each argument should have default values. youTube() should go into the creators dictionary and change the like, subscribe, or notification count for that channel's entry in the dictionary creators.

```
# creators should look like
creators = {"The Gabbie Show": {"likes":0, "subs": 0, "notifs": 0},
"3Blue1Brown":{"likes":0, "subs": 0, "notifs": 0},
"Extra Credits": {"likes":0, "subs": 0, "notifs": 0},
"Shane Dawson":{"likes":0, "subs": 0, "notifs": 0}}
```
* Create a dictionary called Tamagotchi. It should have the keys health, love, hunger, thirst, play, and tired. Write 4 functions that act on this dictionary.
* -- medicine() should increase the health of the Tamagotchi dictionary by n (an argument that tells you how many health points to add).
* -- sleep() should decrease the tiredness of the Tamagotchi dictionary by 10 for each hour (an argument for sleep()) the Tamagotchi sleeps. Tiredness can't go negative.
* -- walk() should take distance in miles as an argument. Increase the love, hunger, and thirst in the Tamagotchi dictionary. Increase love by 2 for every mile walked. Increase hunger by 10 for every mile walked, and increase thirst by 5 for every mile walked.  
* -- feed() should take in an argument for number of cups of food given. Decrease hunger by 10 for every cup of food given.
* all Tamagotchi functions should have default arguments.
