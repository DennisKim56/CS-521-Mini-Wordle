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

print('                     __   __   __        ___ ')
print(' |\/| | |\ | | |  | /  \ |__) |  \ |    |__  ')  
print(' |  | | | \| | |/\| \__/ |  \ |__/ |___ |___ ')  
print('                                             ')  
print('Welcome to Miniwordle!')

# Initialize context/session vars and methods
game_history = dict()
exit_game = False

def print_feedback(data):
    print(data)

def play_game():
    # Initialize game object
    game = Game(word_list, game_history)
    # game.print_secret_word()
    while(game.is_ongoing()):
        guess = input(f'[Guess #{game.current_guess()}] Enter a four letter word: ')
        if game.validate(guess, word_list):
            feedback = game.evaluate(guess)
            print_feedback(feedback)
    game_history[hash(game)] = 'Done'

while not exit_game:
    print('1. Play a new game')
    print('2. See scores')
    print('3. Help')
    print('4. Exit')
    user_input = input('--> Please select an option: ')
    if user_input == '1':
        play_game()
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        exit_game = True
    else:
        print('Input not recognized. Enter "1" to play a new game, "2" to see '+
              'high scores, or "3" to exit.')