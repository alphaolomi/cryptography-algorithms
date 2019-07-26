# Transposition Cipher Decryption

import math


def main():
    my_message = 'Cenoonommstmme oo snnio. s s c'
    my_key = 8
    plaintext = decrypt_message(my_key, my_message)
    # Print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + '|')


def decrypt_message(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.
    # The number of "columns" in our transposition grid:
    num_of_columns = math.ceil(len(message) / key)

    # The number of "rows" in our grid will need:
    num_of_rows = key

    # The number of "shaded boxes" in the last "column" of the grid:
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * num_of_columns

    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1  # point to next column

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)


# the main() function.
if __name__ == '__main__':
    main()
