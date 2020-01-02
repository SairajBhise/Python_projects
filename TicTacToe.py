# game using python     1/1/2020

from IPython.display import clear_output


# Step 1


def display_board(board):
    clear_output()
    print('' + board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print('' + board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print('' + board[1] + '|' + board[2] + '|' + board[3])


# test_board = [''] * 10
# test_board2 = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
# display_board(test_board)


# step2


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 : Choose X or O : ').upper()
        player_1 = marker

    if player_1 == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# player1_marker, player2_marker = player_input()


# step 3


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board2, '$', 8)
# display_board(test_board2)


# Step 4


def win_check(board, mark):
    return (board[1] == mark and board[2] == mark and board[3] == mark) or \
           (board[4] == mark and board[5] == mark and board[6] == mark) or \
           (board[7] == mark and board[8] == mark and board[9] == mark) or \
           (board[9] == mark and board[6] == mark and board[3] == mark) or \
           (board[8] == mark and board[5] == mark and board[2] == mark) or \
           (board[7] == mark and board[4] == mark and board[1] == mark) or \
           (board[1] == mark and board[5] == mark and board[9] == mark) or \
           (board[3] == mark and board[5] == mark and board[9] == mark)


# win_check(test_board2, 'X')

# Step 4


import random


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# step 5


def space_check(board, position):
    return board[position] == ' '


# step 6


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


# step 7


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose position from 1 - 9 : '))

    return position


# step 8


def replay():
    choice = input('Do you want to play again : Yes or no : ').lower()
    return choice == 'yes'


# step 9       2/1/2020


print('Welcome to Tac tac toe')
while True:
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' Will go first')
    play_game = input('Ready to play ? y or n? : ').lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('The player 1 has won the game ')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board()
                    print('Tie game')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('The player 2 has won the game ')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
