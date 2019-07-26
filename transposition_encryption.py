# Transposition Cipher Encryption


def main():
    my_message = 'Common sense is not so common.'
    my_key = 8
    cipher_text = encrypt_message(my_key, my_message)
    # Print the encrypted string in cipher_text to the screen, with
    # a | (called "pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(cipher_text + '|')


def encrypt_message(key, message):
    # Each string in cipher_text represents a column in the grid.
    cipher_text = [''] * key
    # Loop through each column in cipher_text.
    for col in range(key):
        pointer = col
        # Keep looping until pointer goes past the length of the message.
        while pointer < len(message):  # Place the character at pointer in message at the end of the
            # current column in the cipher_text list.
            cipher_text[col] += message[pointer]
            # move pointer over
            pointer += key
            # Convert the cipher_text list into a single string value and return it.
    return ''.join(cipher_text)


# the main() function.
if __name__ == '__main__':
    main()
