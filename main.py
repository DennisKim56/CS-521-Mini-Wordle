'''This code is the entry point into the program and manages the game context
to include reading in a list of all possible words from a file and prompting
user for input'''

import os
import game_class

INPUT_FILENAME = 'word_list.txt'

# Read in word_list text file, if missing, then exit
dir_name  = os.getcwd()
file_name = os.path.join(dir_name, INPUT_FILENAME)
if not os.path.isfile(file_name):
    print(f'--> Error: File is missing. {INPUT_FILENAME} not found')
    exit()
text_file = open(file_name, 'r')
input_file_data = text_file.read()
text_file.close()

word_list = input_file_data.splitlines()

game = game_class.Game(word_list)