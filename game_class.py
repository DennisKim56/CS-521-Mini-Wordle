'''This code defines the 'Game' class which manages the logic necessary to 
govern how the game is played. Upon initialization, a secret word is randomly 
selected from a provided list. This class provides methods for interacting with
the game.'''
import random

class Game:
    # Randomly select word when initialized
    def __init__(self, word_list):
        self.__secret_word = tuple(random.choice(word_list))
        self.guesses = []
        self.ongoing = True

    def validate(self, guess, word_list):
        if not guess.isalpha():
            print('--> Error: Guesses may only contain letters. Please try '
                  +'another guess.')
        elif len(guess) != 4:
            print('--> Error: You may only guess 4-letter words. '+
                  'Please try another word.') 
        elif guess not in word_list:
            print('--> Error: Word not recognized. Please try another word.')
        else:
            pass

    def current_guess(self):
        return len(self.guesses) + 1
    # This function is for testing only and will be removed in prod
    def print_secret_word(self):
        print(self.__secret_word)

    def __hash__(self):
        return hash(self.__secret_word)
