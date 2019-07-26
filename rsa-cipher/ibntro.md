# RSA Ciphers
by @AlSweigart <al@inventwithpython.com>


##Topics Covered In This Chapter:
 Public key cryptography  Man-in-the-middle attacks  ASCII  The chr() and ord() functions  The bytes data type and bytes() function  The encode() string and decode() bytes method  The min() and max() functions  The insert() list method  The pow() function

## example
If Alice wants to send Bob a message, Alice finds Bob’s public key (or Bob can give it to her). Then Alice encrypts her message to Bob with Bob’s public key. Since the public key cannot decrypt a message that was encrypted with it, it doesn’t matter that everyone else has Bob’s public key.
When Bob receives the encrypted message, he uses his private key to decrypt it. If Bob wants to reply to Alice, he finds her public key and encrypts his reply with it. Since only Alice knows her own private key, Alice will be the only person who can decrypt the encrypted message.

## note
Remember that when sending encrypted messages using a public key cipher:
 The public key is used for encrypting.  The private key is used for decrypting

## history
The particular public key cipher that we will implement is called the RSA cipher, which was invented in 1977 and named after its inventors: Ron Rivest, Adi Shamir and Leonard Adleman.



##logic
Generating Public and Private Keys

- A key in the RSA scheme is made of two numbers. There are three steps to creating the keys:
1. Create two random, very large prime numbers. These numbers will be called p and q. Multiply these numbers to get a number which we will call n. 2. Create a random number, called e, which is relatively prime with (p – 1) × (q – 1). 3. Calculate the modular inverse of e. This number will be called d.
The public key will be the two numbers n and e. The private key will be the two numbers n and d. (Notice that both keys have the number n in them.) We will cover how to encrypt and decrypt with these numbers when the RSA cipher program is explained. First let’s write a program to generate these keys.


- Why Can’t We Hack the RSA Cipher All the different types of cryptographic attacks we’ve used in this book can’t be used against the RSA cipher:
1. The brute-force attack won’t work. There are too many possible keys to go through. 2. A dictionary attack won’t work because the keys are based on numbers, not words. 3. A word pattern attack can’t be used because the same plaintext word can be encrypted differently depending on where in the block it appears. 4. Frequency analysis can’t be used. Since a single encrypted block represents several characters, we can’t get a frequency count of the individual characters.
There are no mathematical tricks that work, either. Remember, the RSA decryption equation is:
M = C^d mod n
Where M is the message block integer, C is the ciphertext block integer, and the private key is made up of the two numbers (d, n). Everyone (including a cryptanalyst) has the public key file, which provides (e, n), so the n number is known. If the cryptanalyst can intercept the ciphertext (which we should always assume is possible), then she knows C as well. But without knowing d, it is impossible to do the decryption and calculate M, the original message.
