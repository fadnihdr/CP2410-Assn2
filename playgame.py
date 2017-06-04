""" playgame.py

Contains the Connect 3 game playing application.
This file forms part of the assessment for CP2410 Assignment 2

************** ENTER YOUR NAME HERE ****************************

"""
from connect3board import Connect3Board
from gametree import GameTree


def main():
    print('Welcome to Connect 3 by YOUR NAME HERE')
    mode = get_mode()
    while mode != 'Q':
        if mode == 'A':
            run_two_player_mode()
        elif mode == 'B':
            run_ai_mode()
        mode = get_mode()


def run_two_player_mode():
    columns = 3
    rows = 3
    game = Connect3Board(columns,rows)
    print(game)
    a = True
    while a:
        print(game.get_turn_number())
        print(game.get_whose_turn())
        userInput = get_int("In which column do you want to put?")
        if game.can_add_token_to_column(userInput):
            game.add_token(userInput)
            if game.get_winner():
                print(game.get_whose_turn() + " Wins")
                break
            else:
                print(game)
        else:
            print("cannot lah")
    main()


def run_ai_mode():
    pass


def get_mode():
    mode = input("A. Two-player mode\nB. Play against AI\nQ. Quit\n>>> ")
    while mode[0].upper() not in 'ABQ':
        mode = input("A. Two-player mode\nB. Play against AI\nQ. Quit\n>>> ")
    return mode[0].upper()


def get_int(prompt):
    result = 0
    finished = False
    while not finished:
        try:
            result = int(input(prompt))
            finished = True
        except ValueError:
            print("Please enter a valid integer.")
    return result


if __name__ == '__main__':
    main()
