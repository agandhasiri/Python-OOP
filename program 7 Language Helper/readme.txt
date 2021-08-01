---------------------------------------
Author: akhil.gandhasiri@slu.edu, zainab.alramadhan@slu.edu

---------------------------------------
Approximate number of hours spent: 

20 hrs

---------------------------------------
Citation of any help received from (approved) sources:

None

---------------------------------------
Brief overview of program, including any known bugs:

First, the constructor has an attribute languageSet which is a set. Add all the language words in to the set.

The contains method checks the given word is present in the language set or not.

In the getsuggestions method, first, take a list for all the suggestions. In a new list
add all the strings that has length equal to the length of query string, and strings with 
query length (+1,-1). A for loop to check all the strings with query. In the loop, first, 
if if query is a legitimate word (equal to word in list), add it to the suggestions list.
Then find the length of each word. In the next step, keep the record of the match count,
take a for loop with range of length of query, check if the first letter is upper case letter,
capitalize query and each word if query's first letter is a upper case letter, then check each letter of query in word
and increase the macth count if matches. If first letter of query is not an upper case letter, change query to lower case and
check each letter of query in word and increase the macth count if matches. In the next step after completion of the loop,
compare the match count with the max letter string of query and word, add the word if it is one edit distance.
If match count is one value more than the word, if the word not in suggestions, add the word to the suggestions list.
Now, take a for loop with range of query length -1, check everytime by changing two letters(neighbering letters) till last letter,
if the two letter inverted word is in list of requried strings and not in suggestions, add it to the suggestions.

Return the sorted suggestions list.



