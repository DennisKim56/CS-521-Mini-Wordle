'''This code defines the 'Game' class which manages the logic necessary to 
govern how the game is played. Upon initialization, a secret word is randomly 
selected from a provided list. This class provides methods for interacting with
the game.'''
import random

class Game:
    # Randomly select word when initialized
    def __init__(self, word_list):
        # Secret word should never change
        self.__secret_word = tuple(random.choice(word_list))
        self.guesses = []
        self.ongoing = True

    # Validate that the guess is a real four-letter word
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
            return True
        
    # Generate user feedback for  guess
    def evaluate(self, guess):
        # A perfect match is a correct letter in the correct spot
        perfect_match_count = 0
        # A partial match is a correct letter in the wrong spot
        partial_match_count = 0

        temp_secret = list(self.__secret_word)
        temp_guess = list(guess)
        # Find all perfect matches and remove from the temp vars
        # Note: Comparison must be done in reverse from last to first so that
        # the pop() function doesn't mess up indices for future comparisons
        for i in range(len(self.__secret_word)-1,-1,-1):
            if self.__secret_word[i] == guess[i]:
                temp_secret.pop(i)
                temp_guess.pop(i)
                perfect_match_count += 1
        # Find all partial matches and remove from the temp vars
        for j in range(len(temp_secret)):
            if temp_guess[j] in temp_secret:
                temp_secret.remove(temp_guess[j])
                partial_match_count += 1
        # Return match feedback as dictionary
        feedback={'perfect': perfect_match_count, 'partial':partial_match_count}
        return(feedback)

    # Return the current guess count
    def current_guess(self):
        return len(self.guesses) + 1
    
    # Hash of class is just hash of the secret word
    def __hash__(self):
        return hash(self.__secret_word)
    
    # This function is for testing only and will be removed in prod
    def print_secret_word(self):
        print(self.__secret_word)
