""" playgame.py

Contains the Connect 3 game playing application.
This file forms part of the assessment for CP2410 Assignment 2

************** ENTER YOUR NAME HERE ****************************

"""
from connect3board import Connect3Board
from gametree import GameTree
from timeit import default_timer as timer


def main():
    print('Welcome to Connect 3 by YOUR NAME HERE')
    mode = get_mode()
    while mode != 'Q':
        if mode == 'A':
            run_two_player_mode()
        elif mode == 'B':
            board_testing()
        mode = get_mode()


def run_two_player_mode():
    c = get_int("How many columns?")
    r = get_int("How many rows?")
    start = timer()
    game = Connect3Board(c, r)
    end = timer()
    print(game)
    print(end - start)
    while True:
        print("Turn " + str(game.get_turn_number()))
        print(str(game.get_whose_turn()) + "'s Turn")
        uinput = get_int("In which column do you want to put?")
        if game.can_add_token_to_column(uinput):
            game.add_token(uinput)
            if game.get_winner():
                print(game)
                print(game.get_winner() + " Wins")

                break
            else:

                print(game)
        else:
            print("cannot lah")
    return 0


def run_ai_mode():
    c = get_int("How many columns?")
    r = get_int("How many rows?")
    game = Connect3Board(c, r)
    print(game)


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


def board_testing():
    a = [3, 10, 20, 40, 80, 100, 200, 400, 800, 1000]
    for i in a:
        start = timer()
        game = Connect3Board(i, i)
        end = timer()
        print(end-start)


if __name__ == '__main__':
    main()
