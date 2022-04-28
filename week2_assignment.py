'''
Assignment 1 - Tic-Tac-Toe
Author: Thiago Silva
'''


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
def main():
    print("\n                   █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n                   █---╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗--█\n                   █---║║║╠─║─║─║║║║║╠─--█\n                   █---╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝--█\n                   █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
    print(f"\n{bcolors.HEADER}                 {bcolors.UNDERLINE}Welcome to TIC TAC TOE GAME!{bcolors.ENDC}")
    print()
    print()
    print()
    new_game = str(input("DO YOU WANT TO START A NEW GAME? "))
    while new_game != "yes" and new_game!= "no":
        print("Wrong option, try again!")
        new_game = str(input("DO YOU WANT TO START A NEW GAME? "))
    while new_game == "yes":
        print("\n\n                           ╔╗╔═╦╗\n                           ║╚╣║║╚╗\n                           ╚═╩═╩═╝\n\n")
        x=str(input("NAME OF THE FIRST PLAYER: "))
        print(f"{bcolors.OKBLUE}{x} is the x{bcolors.ENDC}")
        o=str(input("\n\nNAME OF THE SECOND PLAYER: "))
        print(f"{bcolors.OKGREEN}{o} is the x{bcolors.ENDC}")
        player = next_player("")
        tic_tac__toe_board = create_board()
        the_winner=0
        its_a_draw=0
        cont=1
        for cont in range(9):
            if the_winner!=1 and its_a_draw!=1:
                display_board(tic_tac__toe_board)
                current_player = player
                player_move(player, tic_tac__toe_board, x, o)
                player = next_player(player)
                the_winner = has_winner(tic_tac__toe_board)            
                its_a_draw = is_a_draw(tic_tac__toe_board)
                print(the_winner)
                print(its_a_draw)
            else:
                break
        display_board(tic_tac__toe_board)
        if the_winner == 1 and its_a_draw!= 1:
            if current_player == "x":
                print(f"{bcolors.OKBLUE}Congratulations {x}, you won the game!.{bcolors.ENDC}") 
                print("\n\n             ╲╭━━━━╮╲╲\n             ╲┃╭╮╭╮┃╲╲\n             ┗┫┏━━┓┣┛╲\n             ╲┃╰━━╯┃ ╲\n             ╲╰┳━━┳╯╲╲\n             ╲╲┛╲╲┗╲╲╲\n\n")
            else:
                print(f"{bcolors.OKGREEN}Congratulations {o}, you won the game!.{bcolors.ENDC}") 
                print("\n\n             ╲╭━━━━╮╲╲\n             ╲┃╭╮╭╮┃╲╲\n             ┗┫┏━━┓┣┛╲\n             ╲┃╰━━╯┃ ╲\n             ╲╰┳━━┳╯╲╲\n             ╲╲┛╲╲┗╲╲╲\n\n")
        else:
            print("\nIt's a draw!\n")
        new_game = str(input("DO YOU WANT TO START A NEW GAME? "))
        
        
    print("HOPE YOU PLAY AGAIN SOON!")

def create_board():
    tic_tac__toe_board = []
    for square in range(9):
        tic_tac__toe_board.append(square + 1)
    return tic_tac__toe_board

def display_board(tic_tac__toe_board):
    print()
    print(f"{tic_tac__toe_board[0]}|{tic_tac__toe_board[1]}|{tic_tac__toe_board[2]}")
    print('-+-+-')
    print(f"{tic_tac__toe_board[3]}|{tic_tac__toe_board[4]}|{tic_tac__toe_board[5]}")
    print('-+-+-')
    print(f"{tic_tac__toe_board[6]}|{tic_tac__toe_board[7]}|{tic_tac__toe_board[8]}")
    print()
    
def is_a_draw(tic_tac__toe_board):
    for square in range(9):
        if tic_tac__toe_board[square] != "x" and tic_tac__toe_board[square] != "o":
            return 0
    return 1 
    
def has_winner(tic_tac__toe_board):
    if (tic_tac__toe_board[0] == tic_tac__toe_board[1] == tic_tac__toe_board[2] or
        tic_tac__toe_board[3] == tic_tac__toe_board[4] == tic_tac__toe_board[5] or
        tic_tac__toe_board[6] == tic_tac__toe_board[7] == tic_tac__toe_board[8] or
        tic_tac__toe_board[0] == tic_tac__toe_board[3] == tic_tac__toe_board[6] or
        tic_tac__toe_board[1] == tic_tac__toe_board[4] == tic_tac__toe_board[7] or
        tic_tac__toe_board[2] == tic_tac__toe_board[5] == tic_tac__toe_board[8] or
        tic_tac__toe_board[0] == tic_tac__toe_board[4] == tic_tac__toe_board[8] or
        tic_tac__toe_board[2] == tic_tac__toe_board[4] == tic_tac__toe_board[6]):
        return 1
    

    
def player_move(player, tic_tac__toe_board, x, o):
    square = square_func(player, x, o)
    while square<1 or square>9:
        display_board(tic_tac__toe_board)
        print(f"{bcolors.FAIL}Wrong number, try again!{bcolors.ENDC}")
        square = square_func(player, x, o)
    while tic_tac__toe_board[square - 1]== "x" or tic_tac__toe_board[square - 1]=="o":
        display_board(tic_tac__toe_board)
        print(f"{bcolors.FAIL}Wrong choice, this number was already choosen, try again.{bcolors.ENDC}")
        square = square_func(player, x, o)
    tic_tac__toe_board[square - 1] = player


def square_func(player, x, o):    
    if player == "x":
        square = int(input(f"{bcolors.OKBLUE}It is {x}'s turn, please choose a number (1-9): {bcolors.ENDC}"))
    else:
        square = int(input(f"{bcolors.OKGREEN}It is {o}'s turn, please choose a number (1-9): {bcolors.ENDC}"))
    
    return square


def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()