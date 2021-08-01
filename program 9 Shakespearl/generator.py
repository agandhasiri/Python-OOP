import random


class Generator:
    """Generates random text based on k-grams of an existing sample."""

    def __init__(self, source, k):
        """Construct a new generate using the source string and model of k-grams."""

        self._ngrams = { }
        self._k = k
        self._previousChar = ""
        self._source = source

        for i in range(len(self._source) - self._k):                    # A loop through all the text in the file - given k letters

            k_mer = self._source[i : i+k]                               # k-mer 

            if k_mer not in self._ngrams:                               # if kmer isn't in ngrams, add the kmer  in to the ngrams as dictionary with the next character
                self._ngrams[k_mer] = {self._source[i + k] : self._source.count(self._source[i : i+k+1])}    # and no of times the character occurs


            elif k_mer in self._ngrams:                                 # if kmer is already in dictionary, and next character is not present, add it next to the present characters
                self._ngrams[k_mer][self._source[i + k]] = self._source.count(self._source[i : i+k+1])

            if k_mer == self._source[-self._k :]:                       # if "" is the next char( kmer is at last ), add it as count 1 
                self._ngrams[k_mer][""] = 1




    def nextChar(self):
        """Generate and return an additional character, given current state."""

        if len(self._previousChar) < self._k:                   # for the first n calls, return the first n characters of the original or adds it to the prev char
            self._previousChar += (self._source[len(self._previousChar)])
            return self._previousChar[-1:]

        else:
            presentKmer = self._previousChar[-self._k : ]                # set the current kmer for calculating the next character

            if presentKmer == self._source[-self._k : ]:
                return ""                                                # if the next character is at the end

            for_Next_Char = ""                                           # add all the characters multiplid by it's count
            for key, value in self._ngrams[presentKmer].items():         # call the items of current kmer
                for_Next_Char += key * value

            self._previousChar += random.choice(for_Next_Char)           # add a random character
            return self._previousChar[-1:]

