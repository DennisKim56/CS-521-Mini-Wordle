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
    ''' Based on feedback dictionary, format feedback response for user '''
    if type(data) is str:
        feedback_str = data
    else:
        feedback_str = '           '
        if data['perfect'] + data['partial'] == 0:
            feedback_str += 'None of those letters are in the secret word.'
        else:
            if data['perfect'] == 1:
                feedback_str += (f'{data["perfect"]} letter is in the right '
                                 +'spot. ')
            elif data['perfect'] != 0:
                feedback_str += (f'{data["perfect"]} letters are in the right '
                                 +'spot. ')
            if data['partial'] == 1:
                feedback_str += (f'{data["partial"]} letter is in the wrong '
                                 +'spot. ')
            elif data['partial'] != 0:
                feedback_str += (f'{data["partial"]} letters are in the wrong '
                                +'spots. ')
            if data['partial'] + data['perfect'] == 3:
                feedback_str += '1 letter does not exist in the secret word.'
            elif data['partial'] + data['perfect'] < 3:
                feedback_str += (f'{4 - data["partial"] - data["perfect"]} '
                                +'letters do not exist in the secret word')
    print(feedback_str)

def show_game_history():
    ''' Formats and displays score history '''
    os.system('cls')
    print(' ')
    print('███████╗ ██████╗ ██████╗ ██████╗ ███████╗███████╗')
    print('██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝')
    print('███████╗██║     ██║   ██║██████╔╝█████╗  ███████╗')
    print('╚════██║██║     ██║   ██║██╔══██╗██╔══╝  ╚════██║')
    print('███████║╚██████╗╚██████╔╝██║  ██║███████╗███████║')
    print('╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝')
    print(' ')
    print(' #    Word    Result     Summary')
    print(' -    ----    ------     ----------------------------')
    if len(list(game_history.keys())) == 0:
        print(' ')
        print(' No game history data. Play a game to register scores!')
    else:
        for key, value in game_history.items():
            result = ' Win  ' if value['win'] else ' Loss '
            print(f' {key}    {value["word"]}    {result}     '
                  +f'{ value["summary"]}')
    print(' ')

def show_help():
    ''' Provide information on how to play the game '''
    os.system('cls')
    print('The goal of this game is to try and guess a randomly generated, '
          +'4-letter word within the')
    print('first 10 guesses. After every guess, you will receive feedback '
          +' letting you know how')
    print('close you are to the secret word. While playing the game, you can '
          +'enter "?" to see what')
    print('letters you have already guessed. To start, enter "1" from the '
          +'options menu. You can')
    print('view your scores by entering "2" from  the options menu. Good luck!')
    print(' ')                

def play_game():
    ''' Initializes game class and plays 1 game '''
    os.system('cls')
    # Initialize game object
    game = Game(word_list)
    # game.print_secret_word()
    while game.is_ongoing():
        guess = input(f'[Guess #{game.current_guess()}] Enter a four letter '
                      +'word: ')
        if game.validate(guess):
            feedback = game.evaluate(guess)
            if game.is_ongoing():
                print_feedback(feedback)
            else:
                index = len(list(game_history.keys())) + 1
                game_history[index] = {'word':feedback.upper(), 
                                       'win':bool(game), 
                                       'summary':str(game)}
    print(' ')

while not exit_game:
    ''' Persists game session across game instances '''
    print('1. Play a new game')
    print('2. See scores')
    print('3. Help')
    print('4. Exit')
    user_input = input('---> Please select an option: ')
    if user_input == '1':
        play_game()
    elif user_input == '2':
        show_game_history()
    elif user_input == '3':
        show_help()
    elif user_input == '4':
        exit_game = True
    else:
        print('Input not recognized. Enter "1" to play a new game or "4" to '
              +'exit.')
        