#!/usr/bin/env python
"""
Copyright (C) 2008-2011, Louis G. "Ted" Stern
Sudoku-based password card generator.

Uses sudoku.py from davidbau.com to generate solved puzzle.

It was my first Python project, so be kind with your criticism :-).
"""
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choice, randint, shuffle
from subprocess import Popen, PIPE
from sudoku import solution

def sorted_password():
  # Return an 8 character string with
  # two upper case ascii,
  # three lower case ascii,
  # for a sum of 5 ascii letters,
  # plus 2 digits, for a total of 7 characters.
  nbig = 2
  nsmall = 3
  sp = ''.join( [choice(ascii_uppercase) for x in xrange(  nbig)] +
                [choice(ascii_lowercase) for x in xrange(nsmall)] +
                [choice(digits)          for x in xrange(2)] )
  return sp

def password_grid(board):

  # We don't want to repeat punctuation characters in a grid, so let's
  # shuffle the punctuation string and pick the first 9 out of the shuffle.
  punc  = list(punctuation)
  shuffle(punc)        # in place
  punc = punc[:18]     # first 18 symbols in shuffle

  # Turn the board array into a square matrix (row-wise ordering)
  bmatrix = [ board[i:i+9] for i in xrange(0,81,9) ]

  # Create the horizontal table divider
  divider = "+" + ("-" * 7 + "+") * 3

  out = []  # initialize list

  for row in xrange(9):

    # Add a horizontal divider every 3 rows
    if row % 3 == 0:  out += [divider]

    # Add 2 punctuation characters to the sorted password
    spasswd = sorted_password() + punc[2*row] + punc[2*row+1]

    # Initialize the row string:
    rowstring = ""

    for col in xrange(9):

      # Vertical divider every 3 columns
      if col % 3 == 0:  rowstring += "| "

      # Add character from sorted password,
      # permuted by sudoku row, with a space appended for formatting.
      rowstring += spasswd[bmatrix[row][col]] + " "

    # Add a vertical divider at the end of the row:
    rowstring += "|"

    # Row is complete, now add the string to the list of rowstrings.
    out += [rowstring]

  # Add a final divider at the bottom of the grid
  out += [divider]

  return out

# Tweak the randomization in the sudoku generator:
def randomboard():
  answer = None
  while answer == None:
    # Seed the puzzle with randomly arranged 3x3 cells on the diagonal
    cell11 = [i for i in xrange(9)]; shuffle(cell11)
    cell22 = [i for i in xrange(9)]; shuffle(cell22)
    cell33 = [i for i in xrange(9)]; shuffle(cell33)
    answer = solution(cell11[0:3] + [None]*6 +
                      cell11[3:6] + [None]*6 +
                      cell11[6:9] + [None]*9 +
                      cell22[0:3] + [None]*6 +
                      cell22[3:6] + [None]*6 +
                      cell22[6:9] + [None]*9 +
                      cell33[0:3] + [None]*6 +
                      cell33[3:6] + [None]*6 +
                      cell33[6:9] + [None]*6 )
  return answer

def password_card():
  mycard = []
  for i in xrange(2):
    mycard += [password_grid(randomboard())]

  ngrids = len(mycard)
  nrows = len(mycard[0])

  # convert the list of lists into one long string:
  mystring = '\n'.join([
    ''.join([mycard[i][row] for i in xrange(ngrids)])
    for row in xrange(nrows)])

  return mystring

if __name__ == "__main__":

  # Loop until the password card looks good enough
  while True:
    pcard = password_card()
    print pcard
    print
    if raw_input("Like it? [y/N] ") in ['y','Y']: break

  # Exit if no print desired.
  if raw_input("Print it? [y/N] ") in ['y','Y']:

    # Print out 3 pages in large Courier14 for workstations,
    # and 3 pages in smaller Courier8 to laminate and keep in
    # your wallet or badge holder.
    font = ["Courier14", "Courier8"]
    for i in xrange(2):
      # Pipe the pcard string into enscript to create 3 big pages:
      p = Popen("enscript -# 3 -f " + font[i],
                shell=True,
                stdin=PIPE,stdout=PIPE,stderr=PIPE)

      output, error = p.communicate(pcard)
      print error.rstrip()
