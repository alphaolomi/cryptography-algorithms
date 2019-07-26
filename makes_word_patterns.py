# Makes the wordPatterns.py File
# Creates word_patterns.py based on the words in our dictionary
# text file, dictionary.txt.
# (Download this file from http://invpy.com/dictionary.txt)
import pprint
from typing import TextIO


def get_word_pattern(word):
    # Returns a string of the pattern form of the given word.
    # e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
    word = word.upper()
    next_num = 0
    letter_nums = {}
    word_pattern = []
    for letter in word:
        if letter not in letter_nums:
            letter_nums[letter] = str(next_num)
            next_num += 1
            word_pattern.append(letter_nums[letter])
    return '.'.join(word_pattern)


def main():
    all_patterns = {}
    dict_file: TextIO = open('dictionary.txt')
    word_list = dict_file.read().split('\n')
    dict_file.close()

    for word in word_list:
        # Get the pattern for each string in word_list.
        pattern = get_word_pattern(word)
        if pattern not in all_patterns:
            all_patterns[pattern] = [word]
        else:
            all_patterns[pattern].append(word)

    # This is code that writes code. The wordPatterns.py file contains
    # one very, very large assignment statement.
    file: TextIO = open('word_patterns.py', 'w')
    file.write('all_patterns = ')
    file.write(pprint.pformat(all_patterns))
    file.close()


if __name__ == '__main__':
    main()
