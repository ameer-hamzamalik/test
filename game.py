import random

def draw_game_board(board):  #Board will be a list
    '''board is a list of 10 string'''
    print(f'{board[7]} | {board[8]} | {board[9]} ')
    print('--+---+--')
    print(f'{board[4]} | {board[5]} | {board[6]} ')
    print('--+---+--')
    print(f'{board[1]} | {board[2]} | {board[3]} ')

# lst= [' '] * 10
# draw_game_board(lst)

def input_player_letter():
    letter=''
    while not (letter =='X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter=input().upper()
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']
    
# computer_letter, player_letter = input_player_letter()
# print(computer_letter)

def who_goes_first():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def make_move(board,letter,move):
    board[move]= letter