'''This code defines the 'Game' class which manages the logic necessary to 
govern how the game is played. Upon initialization, a secret word is randomly 
selected from a provided list. This class provides methods for interacting with
the game.'''
import random

class Game:
    def __init__(self, word_list):
        self.__secret_word = random.choice(word_list)
        self.ongoing = True

    def validate(self, guess, word_list):
        if guess not in word_list:
            print('Error')
    # This function is for testing only and will be removed in prod
    def print_secret_word(self):
        print(self.__secret_word)
