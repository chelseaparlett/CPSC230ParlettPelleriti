# STATS.py
Write a program that continually prompts the user for positive integer values and stores them in a list.  You should stop prompting when the user enters a negative integer value.

When the user is done entering values, you should print the list of integers they have provided in sorted order.  You should then compute the mean and standard deviation of the values in the list and print them.

Recall that the mean is just the arithmetic average...the sum of all the values divided by the number of values.  

In statistics, standard deviation is the square root of variance and measures how much, on average, values deviate from the mean.  So consider a list of N numbers, with mean mu.

Variance =  The SUM of all the *mean centered* squares. For each number  in your list,  subtract the mean and  square it. Add  ALL of  those together. [link](https://www.sciencebuddies.org/science-fair-projects/science-fair/variance-and-standard-deviation)

Standard Deviation = SquareRoot of Variance

You should not be using any built in modules that calculate variance/standard deviation for you, you need to code this on your own. But you may use math.sqrt() and sum()

# GEOM.py

In  one  file, geometry.py, write FOUR pieces of code to compute the area of a circle, the circumference of a circle, the volume of a sphere, and the volume of a cylinder given proper inputs. Test.

# MAKEOdd.py

Write a function  makeOdd() that  takes in a list of numbers as an argument. Check  every item  to see if it's odd. If it's not odd, find a consistent way  to make it odd (don't overthink this). Return a list with these new ALL odd values.
