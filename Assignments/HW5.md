# Encrypt
In this assignment, you will get practice with files by implementing a simple encryption
algorithm for a text file.
<br>
<br>
One of the most basic encryption algorithms possible is to simply replace a letter in the
alphabet with another letter. The only constraint is that this replacement must be one-to-one:
every letter can only be replaced by the same letter throughout the text.
<br>
<br>
Suppose you have a file, *replace.txt*, that specifies the replacement for every lowercase and
uppercase letter in the alphabet. This file consists of 52 rows (26 for lowercase, 26 for
uppercase) of the following form:
<br>
X Y
j l
<br>
This is interpreted to mean X is replaced by Y, and j is replaced by l. So basically *replace.txt* is just providing a
mapping of characters in the unencrypted text to characters in the encrypted text. (At this
point you should be thinking about dictionaries…)
Your job is to write two functions to encrypt and decrypt a file using the scheme above.
<br>
<br>
The first function, **encrypt**, will take in the file path of an unencrypted file (as a string) and a file path to your replacement/mapping file (also as a string) as parameters. You should read the unencrypted file and apply the mapping. After encrypting, your function should write the encrypted text to another file, *encrypted.txt*.
<br>
<br>
The second function, **decrypt**, will take the filepath of an encrypted file (as a string) as an argument, along with the filepath to the same replace/mapping file (as a string) as used to encrypt it. You will read the encrypted file, reverse the mapping, and output the result to *unencrypted.txt*.

To make things easier, you need not worry about encrypting or un-encrypting any
characters not in the mapping file (eg. punctuation). Punctuation should however remain in
all files (For example, just leave an "!" as an "!"). Your functions need not return anything since they are writing to files.

This code should work with ANY text file and any replace.txt file (though both files will have the same structure described in the assignment.)
