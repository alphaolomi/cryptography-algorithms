# Frequency Finder
# frequency taken from http://en.wikipedia.org/wiki/Letter_frequency   
# @author A1p5a

englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99,
                     'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
                     'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_letter_count(message):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                   'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                   'Y': 0, 'Z': 0}
    for letter in message.upper():
        if letter in LETTERS:
            letter_count[letter] += 1
            return letter_count


def get_item_at_index_zero(x):
    return x[0]


def get_frequency_order(message):
    # Returns a string of the alphabet letters arranged in order of most
    # frequently occurring in the message parameter.
    # first, get a dictionary of each letter and its frequency count
    letter_to_freq = get_letter_count(message)

    # second, make a dictionary of each frequency count to each letter(s)
    # with that frequency
    freq_to_letter = {}
    for letter in LETTERS:
        if letter_to_freq[letter] not in freq_to_letter:
            freq_to_letter[letter_to_freq[letter]] = [letter]
        else:
            freq_to_letter[letter_to_freq[letter]].append(letter)

    # third, put each list of letters in reverse "ETAOIN" order, and then
    # convert it to a string
    for freq in freq_to_letter:
        freq_to_letter[freq].sort(key=ETAOIN.find, reverse=True)
        freq_to_letter[freq] = ''.join(freq_to_letter[freq])

    # fourth, convert the freq_to_letter dictionary to a list of tuple
    # pairs (key, value), then sort them
    freq_pairs = list(freq_to_letter.items())
    freq_pairs.sort(key=get_item_at_index_zero, reverse=True)

    # fifth, now that the letters are ordered by frequency, extract all
    # the letters for the final string
    freq_order = []
    for freqPair in freq_pairs:
        freq_order.append(freqPair[1])

    return ''.join(freq_order)


def english_frequency_match_score(message):
    # Return the number of matches that the string in the message
    # parameter has when its letter frequency is compared to English
    # letter frequency. A "match" is how many of its six most frequent
    # and six least frequent letters is among the six most frequent and
    # six least frequent letters for English.
    freq_order = get_frequency_order(message)
    match_score = 0
    # Find how many matches for the six most common letters there are.
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freq_order[:6]:
            match_score += 1
            # Find how many matches for the six least common letters there are.
        for uncommonLetter in ETAOIN[-6:]:
            if uncommonLetter in freq_order[-6:]:
                match_score += 1
    return match_score
