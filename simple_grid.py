#!/usr/bin/env python
"""
Just print a 9 x 9 grid of strong passwords
"""
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choice, randint, shuffle

def strong_password():
  # Return an 8 character string with
  # two upper case ascii,
  # three lower case ascii,
  # for a sum of 5 ascii letters,
  # plus 2 digits, for a total of 7 characters.
  nbig = 2
  nsmall = 3
  sp = ([choice(ascii_uppercase) for x in xrange(  nbig)] +
        [choice(ascii_lowercase) for x in xrange(nsmall)] +
        [choice(digits)          for x in xrange(2)] +
        [choice(punctuation)     for x in xrange(2)] )
  shuffle(sp)
  return sp

if __name__ == "__main__":

  for i in xrange(9):
    for c in strong_password():
      print "", c,
    print "\n",
