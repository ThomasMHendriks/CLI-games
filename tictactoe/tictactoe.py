#!/usr/bin/env python
# coding: utf-8


'''
A Tic Tac Toe game for 2 players
By: Thomas Hendriks
'''


def game_board(board):
    #print the current board
    print(f'    {board[6]}  |  {board[7]}  |  {board[8]}')
    print("   " + u'\u2500'*15)
    print(f'    {board[3]}  |  {board[4]}  |  {board[5]}')
    print("   " + u'\u2500'*15)
    print(f'    {board[0]}  |  {board[1]}  |  {board[2]}')


#function for the starting player to select their icon
def chose_icon():
    icon = 'placerholder'
    while icon != 'X' and icon != 'O':
        icon = input("Do you want to play with X or O: ").upper()
        if icon != 'X' and icon != 'O':
            print("That is not one of the options")
        else:
            if icon == '0':
                player_turn = 1
                return player_turn
            else:
                player_turn = 2
                return player_turn


#Check if a player has won the game
def win_check(board):
   if board[0] == board[1] and board[1] == board[2]:
       return True
   elif board[3] == board[4] and board[4] == board[5]:
       return True
   elif board[6] == board[7] and board[7] == board[8]:
       return True
   elif board[0] == board[3] and board[3] == board[6]:
       return True
   elif board[1] == board[4] and board[4] == board[7]:
       return True
   elif board[2] == board[5] and board[5] == board[8]:
       return True
   elif board[0] == board[4] and board[4] == board[8]:
       return True
   elif board[2] == board[4] and board[4] == board[6]:
       return True
   else:
       return False

#function to have the active player select a square


def player_input(board, player_turn):
    choice = False
    while choice == False:
        if player_turn == 1:
            selection = int(input("Time for O to choose (1-9): "))
            #correct selection
            if selection in range(1, 10) and selection in board:
                return (selection-1)
            #wrong selection
            else:
                print('Your selection is incorrect or already taken')
            pass
        elif player_turn == 2:
            selection = int(input("Time for X to choose (1-9): "))
            #correct selection
            if selection in range(1, 10) and selection in board:
                return (selection-1)
            #wrong selection
            else:
                print('Your selection is incorrect or already taken')
                pass

#function to change the board depending on the player's selection


def change_board(decision, player_turn):
    if player_turn == 1:
        board[decision] = 'O'
    else:
        board[decision] = 'X'
    return board

#Alternate players turns


def player_change():
    if player_turn == 1:
        return 2
    else:
        return 1

#Function called to ask the players to keep playing or not


def select_stop():
    choice = input("Do you want to stop playing (type stop): ").lower()
    if choice == 'stop':
        return False
    else:
        print("lets play again")
        return True


#Start the game!
#Player 1 is O, player 2 is X
#Base values:
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
keep_playing = True
winner = False
player_turn = 1
number_of_turns = 0

player_turn = chose_icon()

while keep_playing:
    #Display the current board
    game_board(board)

    #Let the player select a spot to place their mark
    decision = player_input(board, player_turn)

    #Process the player selection on the board
    board = change_board(decision, player_turn)

    #Check for a winner
    winner = win_check(board)
    if winner:
        if player_turn == 1:
            print("\n"*2)
            game_board(board)
            print(f'Congratulations O you have won!')

            #Check wether to keep playing
            keep_playing = select_stop()
            #Reset the base values for the next game
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            winner = False
            number_of_turns = 0

        elif player_turn == 2:
            print("\n"*2)
            game_board(board)
            print(f'Congratulations X you have won!')

            #Check wether to keep playing
            keep_playing = select_stop()
            #Reset the base values for the next game
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            winner = False
            number_of_turns = 0
        else:
            pass

    #Turn count & tie check
    number_of_turns += 1
    if number_of_turns == 9:
        print("Its a Tie!")
        #Check wether to keep playing
        keep_playing = select_stop()
        #Reset the base values for the next game
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        winner = False
        number_of_turns = 0

    #Alternate player turns
    player_turn = player_change()

    # Add some spaces after turn
    if winner == False:
        print("\n"*2)
