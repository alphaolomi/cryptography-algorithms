# RSA Key Generator
  2. # http://inventwithpython.com/hacking (BSD Licensed)  3.   4. import random, sys, os, rabinMiller, cryptomath
The program imports the rabinMiller and cryptomath modules that we created in the last chapter, along with a few others.
Chapter 24 – Public Key Cryptography and the RSA Cipher      387

makeRsaKeys.py
 7. def main():  8.     # create a public/private keypair with 1024 bit keys  9.     print('Making key files...') 10.     makeKeyFiles('al_sweigart', 1024) 11.     print('Key files made.')
