# Instructions

**(Please submit your HW files using the names listed at the begining of each problem.)**

- (**Drink99.py**) Write a function, `song_ninetynine()` that takes two arguments, `n`, and `drink`. Set the default arguments to be `99` and `"beer"`, respectively. The function should **print** out *all* the lyrics of "99 Bottles of Beer on the Wall" ([every verse](https://www.99-bottles-of-beer.net/lyrics.html)) substituting whatever is in `drink` (e.g. `"Kombucha"`, or `"Matcha"`, or `"Soda"`) for Beer, and *starting* at `n` instead of 99. You can assume the user will give you a number greater than or equal to 2. For example, if you call `song_ninetynine(n = 2, drink = "soda")` it should print out:

*2 bottles of soda on the wall, 2 bottles of soda,*
*Take one down, pass it around, 1 bottle of soda on the wall.*

*1 bottle of soda on the wall, 1 bottle of soda,*
*Take one down, pass it around, 0 of soda on the wall*

*0 bottles of soda on the wall, 0 bottles of soda,*
*Go to the store, buy some more, 2 bottles of soda on the wall.*

- (**LoveIsland.py**) Write a function `love_island_couples()` which takes in a list of Love Island contestants, `l`, and **returns** a list of tuples containing all the potential couples (NO REPEATS, e.g. `("Jane", "John")` is the same as `("John", "Jane")`) that could form (assume there are no gender restrictions, i.e. men can pair with anyone: men or women, women can pair with anyone: men or women). In the returned list, each tuple should have the names of the couple members. For example if you called `love_island_couples(["Jack", "Jane", "June", "John"])` you would want to return `[("Jack", "Jane"), ("Jack", "June"), ("Jack", "John"), ("Jane", "June"), ("Jane", "John"), ("June", "John")]` (order of the list and tuples don't matter). The list of contestants can have any length, but will always have 2 or more names. This should work for any list.

- (**Title.py**) Write a function `title_case()` that takes in a string, `s`, and returns that string in Title Case. Title Case (like the title of a book or a paper) has the first letter of every word capitalized, and the rest of the letters lowercase. (Think about what always comes BEFORE the first letter in a word...) Punctuation, spaces, and other non-letter characters should be left as is. For example, if you called `title_case("beta regrESSion and ordinal regression: a toolbox update")` you would want to return `"Beta Regression And Ordinal Regression: A Toolbox Update"`. Set the default value for `s` to be `"O Lord, bless this thy hand grenade, that with it thou mayst blow thine enemies to tiny bits, in thy mercy"`. DO NOT use the builtin python method `.title()`, you should be coding this by hand (though you can use `.upper()`, `.lower()`).

- (**BubbleSort.py**) Write a function, `bubble_sort()` which takes in a list (of any length) and returns the sorted list that has been sorted using the bubble_sort() algorithm (see explanation below). For example, if you call `bubble_sort([4,5,2,3])` it should return `[2,3,4,5]`. You MUST code the bubble sort algorithm, and not use any built in sorting methods/functions.

<img src="https://drive.google.com/uc?export=view&id=1_FbXZMrWxu7bWkxMpW6RBvx6poTNpCsk" alt="BubbleSortExplainer"/>

