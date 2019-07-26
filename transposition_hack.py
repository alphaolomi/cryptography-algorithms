# Transposition Cipher Hacker

from .transposition_decryption import decrypt_message


def main():
    my_message = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri  ch nitaalr eiuengiteehb(e1  
    hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaetee oinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit 
    u1rnd stara nvhn fs edbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  a ihda cctrhe 
    ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna. rteoh add e,D7c1Etnpneehtn beete" evecoal 
    lsfmcrl iu1cifgo ai. sl1rchdnheev sh  meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN 
    eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofg BRe bwlmprraio po  droB 
    wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm -eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn 
    tsigaBmuoetcetias rn """
    hacked_message = hack_transposition(my_message)

    if hacked_message is None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')

    print(hacked_message)


def hack_transposition(message):
    print('Hacking...')
    # Python programs can be stopped at any time by pressing
    # Ctrl-C (on Windows)
    # Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # brute-force by looping through every possible key
    for key in range(1, len(message)):
        print('Trying key #%s...' % key)
        decrypted_text = decrypt_message(key, message)
        if detect_english.isEnglish(decrypted_text):
            # Check with user to see if the decrypted key has been found.
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decrypted_text[:100]))
            print()
        print('Enter D for done, or just press Enter to continue hacking:')
        response = input('> ')
        if response.strip().upper().startswith('D'):
            return decrypted_text
    return None


if __name__ == '__main__':
    main()
