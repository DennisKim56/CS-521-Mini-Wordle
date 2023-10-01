'''This code defines the 'Game' class which manages the logic necessary to 
govern how the game is played. Upon initialization, a secret word is randomly 
selected from a provided list. This class provides methods for interacting with
the game.'''
import random

class Game:
    GUESS_LIMIT = 10

    # Randomly select word when initialized
    def __init__(self, word_list):
        self.__secret_word = tuple(random.choice(word_list))
        # *************************** REMOVE *****************************
        print(self.__secret_word)
        # *************************** REMOVE *****************************
        self.guesses = set()
        self.won_game = False

    # Magic class methods
    def __bool__(self):
        return self.won_game
    def __str__(self):
        status_str = 'Default'
        if self.is_ongoing():
            status_str = 'Game is still ongoing'
        elif self.won_game:
            if len(self.guesses) == 1:
                status_str = f'Solved in {len(self.guesses)} move'
            else:
                status_str = f'Solved in {len(self.guesses)} moves'
        elif len(self.guesses) >= Game.GUESS_LIMIT:
            status_str = f'Unable to solve in {len(self.guesses)} moves'
        return status_str

    # Validate that the guess is a valid four-letter word that hasn't already
    # been guessed
    def validate(self, guess, word_list):
        if not guess.isalpha():
            print('--> Error: Guesses may only contain letters. Please try '
                  +'another guess.')
        elif len(guess) != 4:
            print('--> Error: You may only guess 4-letter words. '
                  +'Please try another word.')
        elif guess in self.guesses:
            print('--> Error: You have already guessed this word. Please try '
                  +'another word.')
        elif guess not in word_list:
            print('--> Error: Word not recognized. Please try another word.')
        else:
            self.guesses.add(guess)
            return True
        
    # Generate user feedback for guess
    def evaluate(self, guess):
        # Perfect = a correct letter in the correct spot
        # Partial = a correct letter in the wrong spot
        perfect_match_count = 0
        partial_match_count = 0

        # Initialize temp vars
        temp_secret = list(self.__secret_word)
        temp_guess = list(guess)
        # Find all perfect matches and remove from the temp vars
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
        # If the word has been solved, notify user and set 'won_game' to True
        if perfect_match_count == 4:
            self.won_game = True
            self.__print_win()
            return self.__secret_word
        
        # If the guess limit has been reached, reveal word and let user know
        # they lost
        if len(self.guesses) >= Game.GUESS_LIMIT:
            self.__print_lose()
            print(f'The secret word was {self.__secret_word}')
            return self.__secret_word
        
        # Return match feedback as dictionary
        feedback={'perfect': perfect_match_count, 'partial':partial_match_count}
        return feedback
    
    # Check if game is still ongoing
    def is_ongoing(self):
        if self.won_game or len(self.guesses) >= Game.GUESS_LIMIT:
            return False
        return True

    # Return the current guess count
    def current_guess(self):
        return len(self.guesses) + 1

    def __print_win(self):
        print(' ')
        print('██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗')
        print('╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║')
        print(' ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║')
        print('  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝')
        print('   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗')
        print('   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝')
        print(' ') 

    def __print_lose(self):
        print(' ')
        print(' ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗██████'
              +'█╗██████╗ ')
        print('██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔═══'
              +'═╝██╔══██╗')
        print('██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗'
              +'  ██████╔╝')
        print('██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝'
              +'  ██╔══██╗')
        print('╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ██████'
              +'█╗██║  ██║')
        print(' ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚═════'
              +'═╝╚═╝  ╚═╝')
        print(' ') 







