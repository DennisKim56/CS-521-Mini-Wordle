import os
import enchant
from itertools import permutations

OUTPUT_FILE = 'word_list.txt'

dir_name  = os.getcwd()
file_name = os.path.join(dir_name, OUTPUT_FILE)

# Initialize dictionary
d=enchant.Dict("en_US")
word_set = list()
letter_list = list('abcdefghijklmnopqrstuvwxyz')
word_list = list(permutations(letter_list,4))
for word in word_list:
    word_string = "".join(word)
    if d.check(word_string):
        word_set.append(word_string)

word_set.sort()
output_file = open(file_name, 'w')
for word in word_set:
    output_file.write(word+'\n')
output_file.close()
print("Success!")