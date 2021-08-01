---------------------------------------
Authors: akhil.gandhasiri@slu.edu

---------------------------------------
Approximate number of hours spent:

20 hrs

---------------------------------------
Citation of any help received from (approved) sources:

None

---------------------------------------
Brief overview of program, including any known bugs:

for the generator method, first take a loop through all the text in th file. note the kmer (k characters).
Take a dictionary for all the ngrams. if the kmer is not in the dict, add it with it's  next character and its count
(no of times the character occurs). if the kmer is in the ngrams dict, add it's next character if not present as an
associated value. if the kmer is at the end of the data, add "" as the next character as associated value.

in the nextchar method, for the first k calls, return the first k characters of the original or add it to the
previous characters. set currentkmer for the calculation of the next character, if the next character is at
the end of the source return "". get the items of the current kmer from the ngrams dict.
multiply the characters of the kmer with its count and add it for  choosing the next character.
import random and choose a random value from the characters.



