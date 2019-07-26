# Vigenere Cipher Hacker
import itertools
import re

import vigenereCipher
import pyperclip
import freqAnalysis
import detectEnglish

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SILENT_MODE = False  # if set to True, program doesn't print attempts
NUM_MOST_FREQ_LETTERS = 4  # attempts this many letters per subkey
MAX_KEY_LENGTH = 16  # will not attempt keys longer than this
NONLETTERS_PATTERN = re.compile('[^A-Z]')


def main():
    cipher_text = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr 
    kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm 
    ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz 
    at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby 
    Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, 
    lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz 
    qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms 
    umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa 
    rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf 
    Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn 
    eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl 
    jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a 
    tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl 
    Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs 
    rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif 
    vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, 
    fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at 
    ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz 
    tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd. """
    hacked_message = hack_vigenere(cipher_text)
    if hacked_message is not None:
        print('Copying hacked message to clipboard:')
        print(hacked_message)
        pyperclip.copy(hacked_message)
    else:
        print('Failed to hack encryption.')


def find_repeat_sequences_spacings(message):
    # Goes through the message and finds any 3 to 5 letter sequences
    # that are repeated. Returns a dict with the keys of the sequence and
    # values of a list of spacings (num of letters between the repeats).
    # Use a regular expression to remove non-letters from the message.
    message = NONLETTERS_PATTERN.sub('', message.upper())

    # Compile a list of seqLen-letter sequences found in the message.
    seq_spacings = {}  # keys are sequences, values are list of int spacings
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            # Determine what the sequence is, and store it in seq
            seq = message[seqStart:seqStart + seqLen]
            # Look for this sequence in the rest of the message
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    # Found a repeated sequence.
                    if seq not in seq_spacings:
                        seq_spacings[seq] = []  # initialize blank list
                        # Append the spacing distance between the repeated
                    # sequence and the original sequence.
                    seq_spacings[seq].append(i - seqStart)
    return seq_spacings


def get_useful_factors(num):
    # Returns a list of useful factors of num. By "useful" we mean factors
    # less than MAX_KEY_LENGTH + 1. For example, getUsefulFactors(144)
    # returns [2, 72, 3, 48, 4, 36, 6, 24, 8, 18, 9, 16, 12]
    if num < 2:
        return []  # numbers less than 2 have no useful factors
    factors = []  # the list of factors found
    # When finding factors, you only need to check the integers up to
    # MAX_KEY_LENGTH.
    for i in range(2, MAX_KEY_LENGTH + 1):  # don't test 1
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    if 1 in factors:
        factors.remove(1)
    return list(set(factors))


def get_item_at_index_one(x):
    return x[1]


def get_most_common_factors(seq_factors):
    # First, get a count of how many times a factor occurs in seq_factors.
    factor_counts = {}  # key is a factor, value is how often if occurs

    # seq_factors keys are sequences, values are lists of factors of the
    # spacings. seq_factors has a value like: {'GFD': [2, 3, 4, 6, 9, 12,
    # 18, 23, 36, 46, 69, 92, 138, 207], 'ALW': [2, 3, 4, 6, ...], ...}
    for seq in seq_factors:
        factor_list = seq_factors[seq]
        for factor in factor_list:
            if factor not in factor_counts:
                factor_counts[factor] = 0
            factor_counts[factor] += 1

    # Second, put the factor and its count into a tuple, and make a list
    # of these tuples so we can sort them.
    factors_by_count = []
    for factor in factor_counts:
        # exclude factors larger than MAX_KEY_LENGTH
        if factor <= MAX_KEY_LENGTH:
            # factors_by_count is a list of tuples: (factor, factorCount)
            # factors_by_count has a value like: [(3, 497), (2, 487), ...]
            factors_by_count.append((factor, factor_counts[factor]))

    # Sort the list by the factor count.
    factors_by_count.sort(key=get_item_at_index_one, reverse=True)
    return factors_by_count


def kasiski_examination(cipher_text):
    # Find out the sequences of 3 to 5 letters that occur multiple times
    # in the cipher_text. repeatedSeqSpacings has a value like:
    # {'EXG': [192], 'NAF': [339, 972, 633], ... }
    repeated_seq_spacings = find_repeat_sequences_spacings(cipher_text)

    # See getMostCommonFactors() for a description of seq_factors.
    seq_factors = {}
    for seq in repeated_seq_spacings:
        seq_factors[seq] = []
        for spacing in repeated_seq_spacings[seq]:
            seq_factors[seq].extend(get_useful_factors(spacing))
    # See getMostCommonFactors() for a description of factors_by_count.
    factors_by_count = get_most_common_factors(seq_factors)
    # Now we extract the factor counts from factors_by_count and
    # put them in all_likely_key_lengths so that they are easier to
    # use later.
    all_likely_key_lengths = []
    for twoIntTuple in factors_by_count:
        all_likely_key_lengths.append(twoIntTuple[0])
    return all_likely_key_lengths


def get_nth_subkeys_letters(n, key_length, message):
    # Returns every Nth letter for each key_length set of letters in text.
    # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
    #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
    #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
    #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'
    # Use a regular expression to remove non-letters from the message.
    message = NONLETTERS_PATTERN.sub('', message)

    i = n - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += key_length
    return ''.join(letters)


def attempt_hack_with_key_length(cipher_text, most_likely_key_length):
    # Determine the most likely letters for each letter in the key.
    global freq_scores
    cipher_text_up = cipher_text.upper()
    # all_freq_scores is a list of most_likely_key_length number of lists.
    # These inner lists are the freq_scores lists.
    all_freq_scores = []
    for nth in range(1, most_likely_key_length + 1):
        nth_letters = get_nth_subkeys_letters(
            nth, most_likely_key_length, cipher_text_up)
        # freq_scores is a list of tuples like:
        # [(<letter>, <Eng. Freq. match score>), ... ]
        # List is sorted by match score. Higher score means better match.
        # See the englishFreqMatchScore() comments in freqAnalysis.py.
        freq_scores = []
        for possible_key in LETTERS:
            decrypted_text = vigenereCipher.decryptMessage(
                possible_key, nth_letters)
            key_and_freq_match_tuple = (
                possible_key, freqAnalysis.englishFreqMatchScore(decrypted_text))
            freq_scores.append(key_and_freq_match_tuple)
        # Sort by match score
        freq_scores.sort(key=get_item_at_index_one, reverse=True)
    all_freq_scores.append(freq_scores[:NUM_MOST_FREQ_LETTERS])
    if not SILENT_MODE:
        for i in range(len(all_freq_scores)):
            # use i + 1 so the first letter is not called the "0th" letter 
            print('Possible letters for letter %s of the key: ' % (i + 1), end='')
            for freqScore in all_freq_scores[i]:
                print('%s ' % freqScore[0], end='')
            print()  # print a newline
    # Try every combination of the most likely letters for each position 
    # in the key.
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=most_likely_key_length):
        # Create a possible key from the letters in all_freq_scores
        possible_key = ''
        for i in range(most_likely_key_length):
            possible_key += all_freq_scores[i][indexes[i]][0]
            if not SILENT_MODE:
                print('Attempting with key: %s' % possible_key)
        decrypted_text = vigenereCipher.decryptMessage(possible_key, cipher_text_up)
        if detectEnglish.isEnglish(decrypted_text):
            # Set the hacked cipher_text to the original casing.
            orig_case = []
            for i in range(len(cipher_text)):
                if cipher_text[i].isupper():
                    orig_case.append(decrypted_text[i].upper())
                else:
                    orig_case.append(decrypted_text[i].lower())
            decrypted_text = ''.join(orig_case)
            # Check with user to see if the key has been found.
            print('Possible encryption hack with key %s:' % (possible_key))
            print(decrypted_text[:200])  # only show first 200 characters
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decrypted_text
                # No English-looking decryption found, so return None.
    return None


def hack_vigenere(cipher_text):
    # First, we need to do Kasiski Examination to figure out what the
    # length of the ciphertext's encryption key is.
    all_likely_key_lengths = kasiski_examination(cipher_text)
    if not SILENT_MODE:
        key_length_str = ''
        for key_length in all_likely_key_lengths:
            key_length_str += '%s ' % key_length
        print('Kasiski Examination results say the most likely key lengths are: ' + key_length_str + '\n')

    for key_length in all_likely_key_lengths:
        if not SILENT_MODE:
            print('Attempting hack with key length %s (%s possible keys)...' % (
                key_length, NUM_MOST_FREQ_LETTERS ** key_length))
            hacked_message = attempt_hack_with_key_length(cipher_text, key_length)

            if hacked_message is not None:
                break
            # If none of the key lengths we found using Kasiski Examination
            # worked, start brute-forcing through key lengths.
            if hacked_message is None:
                if not SILENT_MODE:
                    print('Unable to hack message with likely key length(s). Brute-forcing key length...')
                for key_length in range(1, MAX_KEY_LENGTH + 1):
                    # don't re-check key lengths already tried from Kasiski
                    if key_length not in all_likely_key_lengths:
                        if not SILENT_MODE:
                            print('Attempting hack with key length %s (%s possible keys)...' % (
                                key_length, NUM_MOST_FREQ_LETTERS ** key_length))
                        hacked_message = attempt_hack_with_key_length(cipher_text, key_length)
                        if hacked_message is not None:
                            break
    return hacked_message


# the main() function.
if __name__ == '__main__':
    main()
