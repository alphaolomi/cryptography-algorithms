# Vigenere Cipher Dictionary Hacker

import detectEnglish, vigenereCipher, pyperclip


def main():
    cipher_text = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hacked_message = hack_vigenere(cipher_text)
    if hacked_message is not None:
        print('Copying hacked message to clipboard:')
        print(hacked_message)
        pyperclip.copy(hacked_message)
    else:
        print('Failed to hack encryption.')


def hack_vigenere(cipher_text: str) -> str:
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()
    for word in words:
        word = word.strip()  # remove the newline at the end
        decrypted_text = vigenereCipher.decryptMessage(word, cipher_text)

        if detectEnglish.isEnglish(decrypted_text, wordPercentage=40):
            # Check with user to see if the decrypted key has been found.
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ': ' + decrypted_text[:100])
            print()
            print('Enter D for done, or just press Enter to continue breaking:')

        response = input('> ')
        if response.upper().startswith('D'):
            return decrypted_text

if __name__ == '__main__':
    main()
