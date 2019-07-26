# Prime Number Sieve
# author: A1p5a

import math


def is_prime(num):
    # Returns True if num is a prime number, otherwise False.
    # Note: Generally, isPrime() is slower than primeSieve().
    # all numbers less than 2 are not prime
    if num < 2:
        return False
        # see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def prime_sieve(sieve_size):
    # Returns a list of prime numbers calculated using
    # the Sieve of Eratosthenes algorithm.
    sieve = [True] * sieve_size
    sieve[0] = False  # zero and one are not prime numbers
    sieve[1] = False
    # create the sieve

    for i in range(2, int(math.sqrt(sieve_size)) + 1):
        pointer = i * 2
        while pointer < sieve_size:
            sieve[pointer] = False
            pointer += i
            # compile the list of primes
    primes = []

    for i in range(sieve_size):
        if sieve[i]:
            primes.append(i)
    return primes
