""" connect3board.py

Contains the definition of the Connect3Board class.
This file forms part of the assessment for CP2410 Assignment 2

************** ENTER YOUR NAME HERE ****************************

"""

import copy
from timeit import default_timer as timer


class Connect3Board:
    TOKENS = ['O', '#']
    DRAW = 'DRAW'

    __slots__ = '_rows', '_cols', '_board', '_turn_number'

    def __init__(self, rows, cols, turn_number=0, board=None):
        self._rows = rows
        self._cols = cols
        self._board = board
        self._turn_number = turn_number
        if board is None:
            self._make_board()

    def get_columns(self):
        """ Returns the number of columns in the board """
        return self._cols

    def get_rows(self):
        """ Returns the number of rows in the board """
        return self._rows

    def get_turn_number(self):
        """ Returns the turn number, starting at 0 """
        return self._turn_number

    def get_whose_turn(self):
        """ Returns the token (O or #) of the player whose turn it is currently"""
        return Connect3Board.TOKENS[self._turn_number % 2]

    def get_winner(self):
        """ Returns None if the game is not complete, DRAW if no more moves can be played and there is no winner,
        or the token (O or #) that has won the game by making three-in-a-r horizontally, vertically, or diagonally."""

        # this only works correctly for 3*3, you will need to implement a solution that works for larger
        # sized boards
        start = timer()
        try:
            for r in range(self._rows):
                for c in range(self._cols):
                    if self._board[r][c] is not None:

                        # vertical
                        if r < self._rows - 2 and (self._board[r][c] == self._board[r + 1][c] == self._board[r + 2][c]):
                            return self._board[r][c]

                            # horizontal
                        if c < self._cols - 2 and (self._board[r][c] == self._board[r][c + 1] == self._board[r][c + 2]):
                            return self._board[r][c]

                            # upward diagonal
                        if c < self._cols - 2 and r >= 2 and (
                                self._board[r][c] == self._board[r - 1][c + 1] == self._board[r - 2][c + 2]):
                            return self._board[r][c]

                            # downward diagonal
                        if c < self._cols - 2 and r < self._rows - 2 and (
                                self._board[r][c] == self._board[r + 1][c + 1] == self._board[r + 2][c + 2]):
                            return self._board[r][c]
        except IndexError:
            print("index error")

        # no winner discovered, so check for draw or otherwise return None
        if self._turn_number >= self._rows * self._cols:
            return Connect3Board.DRAW
        else:
            return None

    def add_token(self, column):
        """ Adds the token of the current player to the board at the indicated column and advances
        the game by one turn. Returns True if successful, False if the turn is not made."""
        assert 0 <= column < self._cols
        token = Connect3Board.TOKENS[self._turn_number % 2]
        if self._board[0][column] is None:
            for r in range(self._rows - 1, -1, -1):
                if self._board[r][column] is None:
                    self._board[r][column] = token
                    self._turn_number += 1
                    return True
        return False

    def can_add_token_to_column(self, column):
        """ Returns true if and only it is possible to add a token to the given column """
        return 0 <= column < self._cols and self._board[0][column] is None

    def make_copy(self):
        """ Returns a copy of the board, at the same turn number, and with the same contents """
        return Connect3Board(self._rows, self._cols, self._turn_number, copy.deepcopy(self._board))

    def __str__(self):
        column_labels = ' ' + ''.join(str(i) for i in range(self._cols))
        rows = [column_labels]
        for r in self._board:
            rows.append('|' + ''.join(c if c is not None else ' ' for c in r) + '|')
        rows.append('-' * (self._cols + 2))
        rows.append(column_labels)
        return '\n'.join(rows)

    def _make_board(self):
        self._board = []
        for i in range(self._rows):
            self._board.append([None] * self._cols)
