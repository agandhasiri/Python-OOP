
class LanguageHelper:                                                                        # A language helper class
    
    """ A language helper, which gives suggestions to the user with one edit distance.
       """
         

    def __init__(self, words):                                                      

        """ The constructor consists a set for all the  legitimate strings.
                """

        self._languageSet =set()
        if type(words) == list or tuple or set:                                                # if it is alist or tuple or set

            for w in words:                                                                    
                self._languageSet.add(w.strip("\n").strip())
        else:
            with open(words) as data:                                                          # if it is file
                for line in data:
                    self._languageSet.add(w.strip("\n").strip())

                        
##   
##        self._languageSet =set()                                                             # a set for all the language words
##        for w in words:                                                                      # a loop to take all the words from a file or list
##            self._languageSet.add(w.strip("\n").strip())                                     # strip empty line and spaces



                    

    def __contains__(self, query):                                                           # a contains method

        """ A contains method to check whether the given string is in the legitimate words or not.
                """
   
        if query in self._languageSet or query[0].lower( ) +query[1:] in self._languageSet:          # check if the given string is in language set or not
            return True                                                                       # return True if present else False
        else:
            return False


    def getSuggestions(self, query):                                                          # a suggestions method for all the suggestions

        """ Suggesting the words which are one edit distance. """

        
        suggestions =[]                                                                       # a new list to add all the suggested words

        j = len(query)                                                                        # find length of the query 
        list_of_req_strings = [i for i in self._languageSet if len(i) in ( j -1, j, j+ 1)]    # a list for required strings with equal lenth of query
                                                                                              # and words with length of query +1 and -1

                                                                               
        for word in list_of_req_strings:                                                      # a for loop to check all the saved strings with query
            if query == word:                                                                 # if query is a legitimate word (equal to word in list)
                suggestions.append(word)                                                      # add it to the suggestions
            n = len(word)                                                                     # find the length of each word
            match_Count = 0                                                                   # keep the count of matched letters
            for i in range(j):                                                                # a for loop with range of length of query
                if query[0].isupper():                                                        # check if the first letter is upper case letter
                    query, word = query.capitalize(), word.capitalize()                       # capitalize query and each word if query's first letter is a upper case letter
                    if query[i] in word:                                                      # then check each letter of query in word
                        match_Count += 1                                                      # increase the macth count if matches
                else:                                                                         # if first letter of query is not an upper case letter
                    query, word = query.lower(), word.lower()                                 # change query and each word to lower case
                    if query[i] in word:                                                      # then check each letter of query in word
                        match_Count += 1                                                      # increase the macth count if matches

            if match_Count == (max(j, n) - 1):                                                # compare the match count with the max letter string of query and word
                suggestions.append(word)                                                      # add the word if it is one edit distance
            if match_Count == len(word)+1:                                                    # if match count is one value more than the word
                if not word in suggestions:                                                   # if the word not in suggestions
                    suggestions.append(word)                                                  # add the word to the suggestions list


        for k in range(j - 1):                                                                # a for loop with range of query length -1
            inverted_char_word = query[:k]+query[k+1]+query[k]+query[(k+2):]                  # check by changing two letters(neighbering letters) till last letter
            if inverted_char_word not in suggestions:                                         # if the changed word not in suggestions
                if inverted_char_word in list_of_req_strings:                                 # and in list_req_strings
                    suggestions.append(inverted_char_word)                                    # add the changed word to the suggestions

        return (sorted(suggestions))                                                          # return the sorted suggestions list


