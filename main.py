'''This code is the entry point into the program and manages the game context
to include reading in a list of all possible words from a file and prompting
user for input'''

import os
from game import Game

INPUT_FILENAME = 'word_list.txt'

# Read in word_list text file, if missing, then exit
dir_name  = os.getcwd()
file_name = os.path.join(dir_name, INPUT_FILENAME)
try:
    text_file = open(file_name, 'r')
    input_file_data = text_file.read()
    text_file.close()
    word_list = input_file_data.splitlines()
except:
    print('Error loading input file')
    exit()

game_history = dict()

print('                     __   __   __        ___ ')
print(' |\/| | |\ | | |  | /  \ |__) |  \ |    |__  ')  
print(' |  | | | \| | |/\| \__/ |  \ |__/ |___ |___ ')  
print('                                             ')  
                                            
                                             


def print_feedback(data):
    print(data)

def play_game():
    # Initialize game object
    game = Game(word_list, game_history)
    # game.print_secret_word()
    while(game.ongoing):
        guess = input(f'[Guess #{game.current_guess()}] Enter a four letter word: ')
        if game.validate(guess, word_list):
            feedback = game.evaluate(guess)
            print_feedback(feedback)
    game_history[hash(game)] = 'Done'

play_game()
play_game()
play_game()
print(game_history)