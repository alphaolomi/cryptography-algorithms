# Simple Substitution Cipher

import sys
import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    translated = ''
    my_message: str = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, ' \
                      'and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, ' \
                      'he is offered something which affords a reason for acting in accordance to his instincts, ' \
                      'he will accept it even on the slightest evidence. The origin of myths is explained in this ' \
                      'way. -Bertrand Russell '

    my_key: str = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    my_mode: str = 'encrypt'  # set to 'encrypt' or 'decrypt'
    check_valid_key(my_key)

    if my_mode == 'encrypt':
        translated: str = encrypt_message(my_key, my_message)
    elif my_mode == 'decrypt':
        translated = decrypt_message(my_key, my_message)

    print('Using key %s' % my_key)
    print('The %sed message is:' % my_mode)
    print(translated)
    print()


def check_valid_key(key: str):
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()
    if key_list != letters_list:
        sys.exit('There is an error in the key or symbol set.')


def encrypt_message(key: str, message: str) -> str:
    return translate_message(key, message, 'encrypt')


def decrypt_message(key: str, message: str) -> str:
    return translate_message(key, message, 'decrypt')


def translate_message(key: str, message: str, mode: str) -> str:
    translated: str = ''
    chars_a = LETTERS
    chars_b = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting.
        # We just need to swap where the key and LETTERS strings are used.
        chars_a, chars_b = chars_b, chars_a

        # loop through each symbol in the message

        for symbol in message:
            if symbol.upper() in chars_a:
                # encrypt/decrypt the symbol
                sym_index = chars_a.find(symbol.upper())

                if symbol.isupper():
                    translated += chars_b[sym_index].upper()
                else:
                    translated += chars_b[sym_index].lower()
            else:
                # symbol is not in LETTERS, just add it
                translated += symbol

    return translated


def get_random_key():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
