'''This code tests two of the methods in the "Game" class using a staged copy
of a "Game" object'''

import unittest
from game import Game

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.word_list = ['test','fake','copy']
        self.test_game = Game(self.word_list)
        self.test_game.__secret_word = 'test'

    def test_validate(self):
        # Verify it accepts valid pareamter 
        test_case1 = self.test_game.validate('test', self.word_list)
        self.assertEqual(test_case1, True)

        # Verify that words not in word list are rejected
        test_case2 = self.test_game.validate('list', self.word_list)
        self.assertEqual(test_case2, False)

        # Verify that words longer than 4 characters are rejected
        test_case3 = self.test_game.validate('tests', self.word_list)
        self.assertEqual(test_case3, False)

        # Verify that words less than 4 characters are rejected
        test_case4 = self.test_game.validate('tes', self.word_list)
        self.assertEqual(test_case4, False)

        # Verify that words with non-letters are rejected
        test_case5 = self.test_game.validate('tes1', self.word_list)
        self.assertEqual(test_case5, False)


    def test_evaluate(self):
        # The secret word is set to 'test'
        # Verify evaluating a correct word returns {'perfect':4,'partial':0}
        test_case1 = self.test_game.evaluate('test')
        self.assertTrue(test_case1 == {'perfect':4,'partial':0})

        # Verify evaluating a word with zero correct letters returns
        # {'perfect':0, 'partial': 0}
        test_case2 = self.test_game.evaluate('dogs')
        self.assertTrue(test_case2 == {'perfect':0,'partial':0})

        # Verify evaluating a correct word returns {'perfect':4,'partial':0}
        test_case3 = self.test_game.evaluate('test')
        self.assertTrue(test_case3 == {'perfect':4,'partial':0})

        # Verify evaluating a correct word returns {'perfect':4,'partial':0}
        test_case4 = self.test_game.evaluate('test')
        self.assertTrue(test_case4 == {'perfect':4,'partial':0})

        # Verify evaluating a correct word returns {'perfect':4,'partial':0}
        test_case5 = self.test_game.evaluate('test')
        self.assertTrue(test_case5 == {'perfect':4,'partial':0})

if __name__ == '__main__':
    unittest.main()