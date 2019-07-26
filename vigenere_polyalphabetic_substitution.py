# Vigenere Cipher (Polyalphabetic Substitution Cipher)


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    translated: str = ''
    my_key: str = 'ASIMOV'
    my_mode: str = 'encrypt'  # set to 'encrypt' or 'decrypt'

    my_message: str = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer 
    scientist. He was highly influential in the development of computer science, providing a formalisation of the 
    concepts of "algorithm" and "computation" with the Turing machine. Turing is widely considered to be the father 
    of computer science and artificial intelligence. During World War II, Turing worked for the Government Code and 
    Cypher School (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head of Hut 8, 
    the section responsible for German naval cryptanalysis. He devised a number of techniques for breaking German 
    ciphers, including the method of the bombe, an electromechanical machine that could find settings for the Enigma 
    machine. After the war he worked at the National Physical Laboratory, where he created one of the first designs 
    for a stored-program computer, the ACE. In 1948 Turing joined Max Newman's Computing Laboratory at Manchester 
    University, where he assisted in the development of the Manchester computers and became interested in 
    mathematical biology. He wrote a paper on the chemical basis of morphogenesis, and predicted oscillating chemical 
    reactions such as the Belousov-Zhabotinsky reaction, which were first observed in the 1960s. Turing's 
    homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the United 
    Kingdom. He accepted treatment with female hormones (chemical castration) as an alternative to prison. Turing 
    died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest determined that 
    his death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, 
    following an Internet campaign, British Prime Minister Gordon Brown made an official public apology on behalf of 
    the British government for "the appalling way he was treated." As of May 2012 a private member's bill was before 
    the House of Lords which would grant Turing a statutory pardon if enacted. """

    if my_mode == 'encrypt':
        translated: str = encrypt_message(my_key, my_message)
    elif my_mode == 'decrypt':
        translated = decrypt_message(my_key, my_message)

    print('%sed message:' % (my_mode.title()))
    print(translated)
    print()


def encrypt_message(key, message):
    return translate_message(key, message, 'encrypt')


def decrypt_message(key, message):
    return translate_message(key, message, 'decrypt')


def translate_message(key, message, mode):
    translated = []  # stores the encrypted/decrypted message string
    key_index = 0
    key = key.upper()
    for symbol in message:  # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[key_index])  # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[key_index])  # subtract if decrypting
                num %= len(LETTERS)  # handle the potential wrap-around
                # add the encrypted/decrypted symbol to the end of translated.
        if symbol.isupper():
            translated.append(LETTERS[num])
        elif symbol.islower():
            translated.append(LETTERS[num].lower())
            key_index += 1  # move to the next letter in the key

        if key_index == len(key):
            key_index = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

    return ''.join(translated)


# the main() function.
if __name__ == '__main__':
    main()
