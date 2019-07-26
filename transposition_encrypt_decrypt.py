# Transposition Cipher Encrypt/Decrypt File

import time
import os
import sys
from .transposition_encryption import encrypt_message
from .transposition_decryption import decrypt_message


def main():
    input_filename = 'frankenstein.txt'
    # BE CAREFUL! If a file with the output_filename name already exists,
    # this program will overwrite that file.
    output_filename = 'frankenstein.encrypted.txt'
    my_key = 10
    my_mode = 'encrypt'  # set to 'encrypt' or 'decrypt'
    translated = ''

    # If the input file does not exist, then the program terminates early.
    if not os.path.exists(input_filename):
        print('The file %s does not exist. Quitting...' % input_filename)
        sys.exit()

        # If the output file already exists, give the user a chance to quit.
    if os.path.exists(output_filename):
        print('This will overwrite the file %s. (C)Continue or (Q)Quit?' % output_filename)
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file 2
    file = open(input_filename)
    content = file.read()
    file.close()
    print('%sing...' % (my_mode.title()))

    # Measure how long the encryption/decryption takes.
    start_time = time.time()

    if my_mode == 'encrypt':
        translated = encrypt_message(my_key, content)
    elif my_mode == 'decrypt':
        translated = decrypt_message(my_key, content)

    total_time = round(time.time() - start_time, 2)

    print('%sion time: %s seconds' % (my_mode.title(), total_time))

    # Write out the translated message to the output file.

    output_file = open(output_filename, 'w')
    output_file.write(translated)
    output_file.close()

    print('Done %sing %s (%s characters).' % (my_mode, input_filename, len(content)))
    print('%sed file is %s.' % (my_mode.title(), output_filename))


# call the main() function.
if __name__ == '__main__':
    main()
