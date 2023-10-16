'''This code tests two of the methods in the "Game" class using a staged copy
of a "Game" object'''

import unittest
from game import Game

class TestGame(unittest.TestCase):
    ''' Creates TestGame class using Game class and unittest module'''

    def setUp(self):
        ''' Initializes TestGame object '''
        self.word_list = ['test']
        self.test_game = Game(self.word_list)
        self.test_game.__secret_word = 'test'

    def test_validate(self):
        ''' Method takes in no parameters and executes predefined unit tests
        for the validate() method in Game class'''
        # Verify it accepts valid pareamter 
        test_case1 = self.test_game.validate('test')
        self.assertEqual(test_case1, True)

        # Verify that words not in word list are rejected
        test_case2 = self.test_game.validate('list')
        self.assertEqual(test_case2, False)

        # Verify that words longer than 4 characters are rejected
        test_case3 = self.test_game.validate('tests')
        self.assertEqual(test_case3, False)

        # Verify that words less than 4 characters are rejected
        test_case4 = self.test_game.validate('tes')
        self.assertEqual(test_case4, False)

        # Verify that words with non-letters are rejected
        test_case5 = self.test_game.validate('tes1')
        self.assertEqual(test_case5, False)


    def test_evaluate(self):
        ''' Method takes in no parameters and executes predefined unit tests
        for the evaluate() method in Game class'''

        # Verify evaluating a word with zero correct letters returns
        # {'perfect':0, 'partial': 0}
        test_case2 = self.test_game.evaluate('copy')
        self.assertTrue(test_case2 == {'perfect':0,'partial':0})

        # Verify evaluating a word with 1 partially correct letter returns
        # {'perfect':0, 'partial': 1}
        test_case3 = self.test_game.evaluate('dogs')
        self.assertTrue(test_case3 == {'perfect':0,'partial':1})

        # Verify evaluating a word with 1 perfectly correct letter returns
        # {'perfect':1, 'partial': 0}
        test_case4 = self.test_game.evaluate('toga')
        self.assertTrue(test_case4 == {'perfect':1,'partial':0})

        # Verify evaluating a word with 1 partially correct letter and 1 
        # perfectly correct letter returns {'perfect':1, 'partial': 1}
        test_case5 = self.test_game.evaluate('take')
        self.assertTrue(test_case5 == {'perfect':1,'partial':1})

if __name__ == '__main__':
    ''' Rune unit tests'''
    unittest.main()

    # Simulate game instance with word list of 'test' and secret word 'test'
    word_list = ['test']
    test_game = Game(word_list)
    test_game.__secret_word = 'test'
    # Test that validate method for input 'test' returns true
    assert test_game.validate('test') == True
    # Test that evaluate method for input 'test' sets win condition to true
    test_game.evaluate('test')
    assert  test_game.won_game == True