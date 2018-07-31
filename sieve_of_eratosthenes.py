#!/usr/bin/env python

import sys

def cross_off(flags, prime):
    "Mark multiple numbers of the 'prime' as not prime"
    to_crossoff = prime * 2;
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
    if len(sys.argv) != 2:
        print "Usage: %s <max integer>"
        exit(1)
    max_ = int(sys.argv[1])
    sieve_of_erat(max_)
