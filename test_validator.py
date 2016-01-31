__author__ = 'Jessy'


import unittest

import validator

##  To do this problem, I got some help by looking at Teacher's code from
##  https://github.com/minneapolis-edu/CamelCaseWithTests

##  make unittest as super class and create a new class called "TestWord" to
##  test out method

class TestWord(unittest.TestCase):


## test split method,
#  when sentence split... it should have four words

    def test_Split(self):

        words = validator.split("My name is Jessy")
        self.assertTrue(len(words),4)


##  testing if the same word is used, even after it was split

        words = validator.split('Add more word')
        wList = ['Add', 'more', 'word']
        self.assertEquals(words, wList)



        words = validator.split('Many spaces in different sentence')
        wList = ['Many', 'space', 'in', ' different', 'sentence']
        self.assertEquals(words, wList)



        words = validator.split(' start spaces ')
        wList = ['start', 'spaces']
        self.assertEqual(words, wList)



##  testing the first word of the sentence will change to all lower case letter
    def testFw(self):

        inOut = {'word': 'word', 'lion': 'lion', 'LION': 'lion', 'lION': 'lion', 'lIoN': 'lion'}

        for wordInput in inOut:
            self.assertEqual(validator.first_word(wordInput), inOut[wordInput])


##  testing if the second word and word after the second word will change the first letter of the word to upper case
## and change the letter after the first letter to lower case letter
    def testCamel (self):
        inOut = {'word': 'Word', 'lion': 'Lion', 'LION': 'Lion', 'lION': 'Lion', 'lIoN': 'Lion'}

        for wordInput in inOut:
            self.assertEqual(validator.camelcase_word(wordInput), inOut[wordInput])




##  testing if the sentence is valid...  if the sentence doesn't contain a single quotation, double quotation, number and
##  minus sign, then return true... otherwise return false

    def testVsentence(self):
        self.assertTrue(validator.valid_sentence('This is Jessy Yeah'))
        self.assertTrue(validator.valid_sentence('THIS IS JESSY YEAH'))
        self.assertTrue(validator.valid_sentence('word'))



        self.assertFalse(validator.valid_sentence("I'm a sentence"))
        self.assertFalse(validator.valid_sentence("Hyphens are banned-in variable names"))
        self.assertFalse(validator.valid_sentence('No "quotes" in variable names'))
        self.assertFalse(validator.valid_sentence("99 unit test on a self"))



















