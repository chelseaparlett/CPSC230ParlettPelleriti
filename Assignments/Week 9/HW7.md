# DNA.py
Write a module,  with a function, **complement()**, that returns the complement of a DNA string. Also provide a function, revComplement that takes a DNA sequence as string input and returns the reverse complement of the sequence as a
string. Recall that the valid alphabet is {A, C, T, G} and that A T and G-C are complements. A reverse complement is found by reversing the input string and replacing every nucleotide
with its complement. This means that your revComplement method should use your  complement method internally rather than duplicating code. Your methods should do
appropriate error checking and return an error message as appropriate. Test your functions with input from the user.
<br>
<br>
For example, if your input is ACTG, your complement should be TGAC and your reverse complement should be CAGT.

# PIGLATIN.py
In one file,  write two functions wordToPig() and nameToPig(). Your wordToPig function will take 1 parameter that converts the word based on the below rules.
<br>
<br>
Your nameToPig function takes 2 input parameters, firstName and lastName, and will use your wordToPig function to do the translation to avoid duplicating code. Your nameToPig function returns the names in pig Latin. Test your functions with input from the user, you only need test a name, not a word and then a name.

Please use the following guidelines for Pig Latin:
* **Words beginning with consonants**: move the consonant from the start of the word to the end of the word. Then add the suffix "ay" to the end of the word. For example,
the word "hello" would become ellohay, the word "duck" would become uckday.
* * For a bonus, remove all consonants from the start of the word to the end of
the word and then add the suffix “ay” to the end. For example, “Chapman”
becomes Apmanchay.
* **Words beginning with vowels**: all you need to do is add "yay" to the end of the
word. You don't need to change any letters around, just say the word as normal then add "yay" to the end. For example: the word "egg" becomes eggyay and the word "ultimate" becomes ultimateyay.
Make sure to use your string methods so you have capital letters where appropriate and not otherwise. Test your functions with input from the user. Assume the user enters his/her name with capitals for both their first and last name.

# STRIP.py
Write a function, my_strip() that mimics the .strip() method. It should look for new lines ("\n"), spaces, and tabs ("\t") at the beginning and end of a  string and  remove them. Then return the stripped string.