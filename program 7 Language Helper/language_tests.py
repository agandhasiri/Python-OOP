
from language_tools import LanguageHelper
import unittest

# We define the custom lexicon that we will use for our controlled tests
sample = ('car', 'cat', 'Cate', 'cater', 'care',
          'cot', 'cute', 'dare', 'date', 'dog', 'dodge',
          'coffee', 'pickle', 'grate')

rhymesWithDog = ('bog', 'cog', 'clog', 'fog', 'frog', 'hog', 'log')

testingWords = ('hat', 'mat', 'bat', 'Apple', 'amazing', 'banana', 'written', 'Kattis', 'high-rise',
                'bloth', 'cloth', 'far', 'fan', 'fat', 'kite', 'bite', 'site', 'lite',
                'white', 'hit', 'fight', 'night', 'right', 'bright', 'sight',
                'light', "unnecessary", 'possible', 'impossible', 'weird','rustic')


class BasicTest(unittest.TestCase):

    # make sure that all the words in the lexicon are recognized
    def testContainment(self):
        helper = LanguageHelper(sample)
        for w in sample:
            self.assertTrue(w in helper)

    def testFailures(self):
        helper = LanguageHelper(sample)
        self.assertFalse('cate' in helper)  # only allowed when capitalized
        self.assertFalse('fox' in helper)  # word is not there
        self.assertFalse('cofee' in helper)  # mis-spell word is not there

    def testSuggestInsertion(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('pikle'), ['pickle'])
        self.assertEqual(helper.getSuggestions('ct'), ['cat', 'cot'])

    
    def testSuggestDeletion(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('gratle'), ['grate'])

    
    def testSugeestionsMany(self):
        helper = LanguageHelper(rhymesWithDog)
        self.assertEqual(helper.getSuggestions('rog'), ['bog', 'cog', 'fog', 'frog', 'hog', 'log'])

    
    def testSugeestionsCapitalization(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('Gate'), ['Cate', 'Date', 'Grate'])

    def testSuggestionsNone(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('blech'), [])

    ####################################################################################################################

    

    def testFailures1(self):
        helper = LanguageHelper(testingWords)
        self.assertTrue('Fat' in helper)  
        self.assertFalse('apple' in helper)  
        self.assertFalse('amaizing' in helper)  

    def test_01_insertion(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('at'), ['bat', 'fat', 'hat', 'mat'])

    
    def test_02_insertionAtEnd(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('Appl'), ['Apple'])


    def test_03_deletion(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('amaizing'), ['amazing'])
    
    
    def test_04_repeatingLetters(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('Banna'), ['Banana'])

    
    def test_05(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('Katis'), ['Kattis'])

    
    def test_06(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('bloth'), ['bloth', 'cloth'])


    def test_07(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('Tite'), ['Bite', 'Kite', 'Lite', 'Site'])

    def test_08_upperCaseInBetween(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('riGht'), ['bright', 'fight', 'light', 'night', 'right', 'sight'])

    def test_09(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('unneccessary'), ['unnecessary'])

    def test_10(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('mpossible'), ['impossible', 'possible'])

    def test_11_NeighberingChar(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('rutsic'), ['rustic'])


    def test_12(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('wierd'), ['weird'])
    
    def test_13_withHyphen(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('hgh-rise'), ['high-rise'])
        
    def test_14_withOutHyphen(self):
        helper = LanguageHelper(testingWords)
        self.assertEqual(helper.getSuggestions('highrise'), ['high-rise'])




if __name__ == '__main__':
    unittest.main()
