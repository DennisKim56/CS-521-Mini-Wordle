'''This code defines the 'Game' class which manages the logic necessary to 
govern how the game is played. Upon initialization, a secret word is randomly 
selected from a provided list. This class provides methods for interacting with
the game.'''
import random

class Game:
    ''' Game class contains game parameters and game methods'''
    GUESS_LIMIT = 10

    def __init__(self, word_list):
        ''' Constructor randomly selects a word from word_list parameter'''
        self.__secret_word = tuple(random.choice(word_list))
        self.guesses = set()
        self.won_game = False
        self.guessed_letters = set()
        self.word_list = word_list

    # Magic class methods
    def __bool__(self):
        ''' Mage method returns game state when bool() is invoked '''
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

    def validate(self, guess):
        ''' Validate method takes in a string param (guess) and validates that 
        the guess is valid four-letter word that hasn't already been guessed'''
        if guess == '?':
            return True
        elif not guess.isalpha():
            print('--> Error: Guesses may only contain letters. Please try '
                  +'another guess.')
            return False
        elif len(guess) != 4:
            print('--> Error: You may only guess 4-letter words. '
                  +'Please try another word.')
            return False
        elif guess.lower() in self.guesses:
            print('--> Error: You have already guessed this word. Please try '
                  +'another word.')
            return False
        elif guess.lower() not in self.word_list:
            print('--> Error: Word not recognized. Please try another word.')
            return False
        else:
            self.guesses.add(guess)
            self.guessed_letters.update(set(guess))
            return True
        
    def evaluate(self, guess):
        ''' Method takes in a string param (guess) and generates user feedback 
        for guess'''
        if guess == '?':
            letter_list = list(self.guessed_letters)
            letter_list.sort()
            return ' '.join(letter_list).upper()
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
            return ''.join(self.__secret_word)
        
        # If the guess limit has been reached, reveal word and let user know
        # they lost
        if len(self.guesses) >= Game.GUESS_LIMIT:
            self.__print_lose()
            print(f'------------------ The secret word was "'
                  +f'{"".join(self.__secret_word).upper()}" ------------------')
            return ''.join(self.__secret_word)
        
        # Return match feedback as dictionary
        feedback={'perfect': perfect_match_count, 'partial':partial_match_count}
        return feedback
    
    def is_ongoing(self):
        ''' Method takes in no parameters and returns boolean signifying if a 
        game is still going on '''
        if self.won_game or len(self.guesses) >= Game.GUESS_LIMIT:
            return False
        return True

    def current_guess(self):
        ''' Method takes in no parameters and returns current guess count'''
        return len(self.guesses) + 1

    def __print_win(self):
        ''' Method prints stylized "Win" message '''
        print(' ')
        print('██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗')
        print('╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║')
        print(' ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║')
        print('  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝')
        print('   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗')
        print('   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝')

    def __print_lose(self):
        ''' Method prints stylized "Lose" message '''
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