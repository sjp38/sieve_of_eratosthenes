#!/usr/bin/env python

import argparse
import sys

def cross_off(flags, prime):
    "Mark multiple numbers of the 'prime' as not prime"
    # Non-prime numbers are multiple of prime numbers.  Since we marked
    # multiples of all smaller prime numbers as false, 'prime * n' which n is
    # smaller than 'prime' would already marked as false.  So, we can start
    # from 'prime^2'.
    to_crossoff = prime * prime;
    while to_crossoff < len(flags):
        flags[to_crossoff] = False
        to_crossoff += prime

def next_prime(flags, prime):
    "Find next prime number larger than the 'prime'"
    offset = prime + 1
    while offset < len(flags):
        if flags[offset] == True:
            return offset
        offset += 1
    return offset

def sieve_of_erat(max_):
    # If N-th flag is True, N is prime number
    flags = [True] * (max_ + 1)
    flags[0] = False
    flags[1] = False

    prime = 2
    while prime < max_:
        cross_off(flags, prime)
        prime = next_prime(flags, prime)

    for i, flag in enumerate(flags):
        if flag:
            print i

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('max number', metavar='max_number', type=int, nargs=1,
            help='maximum value of prime number')
    max_ = vars(parser.parse_args())['max number'][0]
    sieve_of_erat(max_)
