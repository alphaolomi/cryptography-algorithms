# Simple Substitution Cipher Hacker

import os
import re
import copy
import pprint

from .simple_substitution_cipher import decrypt_message
from .makes_word_patterns import main, get_word_pattern

if not os.path.exists('word_patterns.py'):
    main()  # create the wordPatterns.py file
    import word_patterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile("[^A-Z\s]")


def main():
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr ' \
              'jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao ' \
              'rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px ' \
              'jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm '

    # Determine the possible valid cipher_text translations.
    print('Hacking...')
    letter_mapping = hack_simple_sub(message)

    # Display the results to the user.
    print('Mapping:')
    pprint.pprint(letter_mapping)
    print()
    print('Original cipher_text:')
    print(message)
    print()
    print('Copying hacked message to clipboard:')

    hacked_message = decrypt_with_cipher_letter_mapping(message, letter_mapping)
    print(hacked_message)


def get_blank_cipher_letter_mapping():
    # Returns a dictionary value that is a blank cipher_letter mapping.
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [],
            'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [],
            'Y': [], 'Z': []}


def add_letters_to_mapping(letter_mapping, cipher_word, candidate):
    # The letter_mapping parameter is a "cipher_letter mapping" dictionary
    # value that the return value of this function starts as a copy of.
    # The cipher_word parameter is a string value of the cipher_text word.
    # The candidate parameter is a possible English word that the
    # cipherword could decrypt to.
    # This function adds the letters of the candidate as potential
    # decryption letters for the cipher_letters in the cipher_letter
    # mapping.
    letter_mapping = copy.deepcopy(letter_mapping)

    for i in range(len(cipher_word)):
        if candidate[i] not in letter_mapping[cipher_word[i]]:
            letter_mapping[cipher_word[i]].append(candidate[i])

    return letter_mapping


def intersect_mappings(map_a, map_b):
    # To intersect two maps, create a blank map, and then add only the
    # potential decryption letters if they exist in BOTH maps.
    intersected_mapping = get_blank_cipher_letter_mapping()
    for letter in LETTERS:
        # An empty list means "any letter is possible". In this case just
        # copy the other map entirely.

        if not map_a[letter]:
            intersected_mapping[letter] = copy.deepcopy(map_b[letter])
        elif not map_b[letter]:
            intersected_mapping[letter] = copy.deepcopy(map_a[letter])
        else:
            # If a letter in mapA[letter] exists in map_b[letter], add
            # that letter to intersected_mapping[letter].
            for mappedLetter in map_a[letter]:
                if mappedLetter in map_b[letter]:
                    intersected_mapping[letter].append(mappedLetter)

    return intersected_mapping


def remove_solved_letters_from_mapping(letter_mapping):
    # Cipher letters in the mapping that map to only one letter are
    # "solved" and can be removed from the other letters.

    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B'
    # maps to ['N'], then we know that 'B' must map to 'N', so we can
    # remove 'N' from the list of what 'A' could map to. So 'A' then maps
    # to ['M']. Note that now that 'A' maps to only one letter, we can
    # remove 'M' from the list of letters for every other
    # letter. (This is why there is a loop that keeps reducing the map.)
    letter_mapping = copy.deepcopy(letter_mapping)
    loop_again = True

    while loop_again:
        # First assume that we will not loop again:
        loop_again = False
        # solved_letters will be a list of uppercase letters that have one
        # and only one possible mapping in letter_mapping
        solved_letters = []
        for cipher_letter in LETTERS:
            if len(letter_mapping[cipher_letter]) == 1:
                # If a letter is solved, than it cannot possibly be a potential
                solved_letters.append(letter_mapping[cipher_letter][0])
                # decryption letter for a different cipher_text letter, so we
                # should remove it from those other lists.
        for cipher_letter in LETTERS:
            for s in solved_letters:
                if len(letter_mapping[cipher_letter]) != 1 and s in letter_mapping[cipher_letter]:
                    letter_mapping[cipher_letter].remove(s)

                if len(letter_mapping[cipher_letter]) == 1:
                    # A new letter is now solved, so loop again.
                    loop_again = True
    return letter_mapping


def hack_simple_sub(message):
    intersected_map = get_blank_cipher_letter_mapping()
    cipher_word_list = nonLettersOrSpacePattern.sub('', message.upper()).split()

    for cipher_word in cipher_word_list:
        # Get a new cipher_letter mapping for each cipher_text word.
        new_map = get_blank_cipher_letter_mapping()
        word_pattern = get_word_pattern(cipher_word)
        if word_pattern not in word_pattern.allPatterns:
            continue  # This word was not in our dictionary, so continue.
        # Add the letters of each candidate to the mapping.
        for candidate in word_patterns.allPatterns[word_pattern]:
            new_map = add_letters_to_mapping(new_map, cipher_word, candidate)
            # Intersect the new mapping with the existing intersected mapping.
            intersected_map = intersect_mappings(intersected_map, new_map)
            # Remove any solved letters from the other lists.
        return remove_solved_letters_from_mapping(intersected_map)


def decrypt_with_cipher_letter_mapping(cipher_text, letter_mapping):
    # Return a string of the cipher_text decrypted with the letter mapping,
    # with any ambiguous decrypted letters replaced with an _ underscore.
    # First create a simple sub key from the letter_mapping mapping.
    key = ['x'] * len(LETTERS)

    for cipher_letter in LETTERS:
        if len(letter_mapping[cipher_letter]) == 1:  # If there's only one letter, add it to the key.
            key_index = LETTERS.find(letter_mapping[cipher_letter][0])
            key[key_index] = cipher_letter
        else:
            cipher_text = cipher_text.replace(cipher_letter.lower(), '_')
            cipher_text = cipher_text.replace(cipher_letter.upper(), '_')
            key = ''.join(key)
            # With the key we've created, decrypt the cipher_text.
            return decrypt_message(key, cipher_text)


if __name__ == '__main__':
    main()
