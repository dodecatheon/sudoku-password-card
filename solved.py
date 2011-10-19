#!/usr/bin/env python
"""
Print a solved sudoku puzzle
"""
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import shuffle
from sudoku import solution

def sudoku_grid(board):

  # Turn the board array into a square matrix (row-wise ordering)
  bmatrix = [ board[i:i+9] for i in xrange(0,81,9) ]

  # Create the horizontal table divider
  divider = "+" + ("-" * 7 + "+") * 3

  out = []  # initialize list

  for row in xrange(9):

    # Add a horizontal divider every 3 rows
    if row % 3 == 0:  out += [divider]

    # Initialize the row string:
    rowstring = ""

    for col in xrange(9):

      # Vertical divider every 3 columns
      if col % 3 == 0:  rowstring += "| "

      # Add character from sorted password,
      # permuted by sudoku row, with a space appended for formatting.
      rowstring += str(bmatrix[row][col]+1) + " "

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
  for i in xrange(1):
    mycard += [sudoku_grid(randomboard())]

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

