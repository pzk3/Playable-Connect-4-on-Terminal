# DO NOT modify or add any import statements
from typing import Optional
from a1_support import *


# Write your classes and functions here

def main() -> None:
    """
    Description: Main function, starts the game and allows for the next new game.
    This can be prompted with either a "y" or a "n" to choose whether the player would
    like to play again.

    Parameters: 
        None

    Return: 
        None
    """
    play_game()
    #prompts for a new game
    while True:
        choice = input(CONTINUE_MESSAGE)
        if choice.lower() == 'y' or not 'n':
            play_game()
        else:   
           break

def num_hours() -> float:
    """
    Description: Check the number of hours estimated to have worked on the assignment.

    Parameters:
        None

    Return: 
        Float: Returns the number of hours estimated to have worked on assignment.
    """
    number_hours = float(20)
    return number_hours

def generate_initial_board() -> list[str]:
    """
    Description: Generates the initial board for the connect 4 game.

    Parameters:
        None

    Return: 
        list[str]: Returns list of strings, which represents the intital board state.
    """
    
    initial_board=['--------', '--------', '--------', '--------', '--------',
    '--------','--------', '--------']
    return initial_board

def is_column_full(column:str) -> bool:
    """
    Description: Function to test if a column in the board is full.

    Parameters: 
        column: string: The specified column to check is represented as a string.

    Return: 
        bool: Returns False if column is empty (there is "-" in the column)
            Returns True overwise
    """
    column_list= list(column)
    #check if the column is full
    if "-" in column_list:
        return False
    else:
        return True

def is_column_empty(column: str) -> bool:
    """
    Description: Checks if a specfied column on the board is empty.

    Parameters: 
        column: string: Specfied column to check is represented as a string. 
    Return: 
        bool: Returns False if column is full (there is not a "-" in the column)
            Returns True overwise
    """
    for char in column:
        #check if column contains space
        if char != '-':
            return False
    return True

        
def display_board(board: list[str]) -> None:
    """
    Description: Displays the full game board

    Preconditions: The  input board will contain exactly 8 strings each with
    exactly 8 characters

    Parameters: 
        board: list[str]: Full game board is represented as a list of strings.
    Return: 
        None (only prints the game board)
    """
    #iterate through each row 
    for i in range(BOARD_SIZE):
        column=COLUMN_SEPARATOR
        for row in board:
            #check if the board has sufficient elements for the row index given
            if i < len(row):
                # add element of current row (column index) to the column separator.
                column += row[i] + COLUMN_SEPARATOR
        print(column)
    print(" 1 2 3 4 5 6 7 8 ")

def check_input(command: str) -> bool:
    """
    Description: Check if the input inputted by the user is valid. 

    Parameters: 
        command: str: User's command (input)

    Return: 
        bool: Returns True if commmand is valid, else False.
    """
    input_letters=["a","A", "R", "r"]
    if command == "":
        print(INVALID_FORMAT_MESSAGE)
        return False
    #check first character of the input
    elif command[0] in input_letters:
        #check length of the command
        if len(command)==2:
            if int(command[1]) in range(1, 9):
                return True
            else:
                print(INVALID_COLUMN_MESSAGE)
                return False
        else:
            print(INVALID_FORMAT_MESSAGE)
            return False
    elif command in ["h","H"]:
        return True
    elif command in ["q", "Q"]:
        return True
    else:
        print(INVALID_FORMAT_MESSAGE)
        return False

def get_action() -> str:
    """
    Description: Prompts the uesr to enter a valid command according
    to check_input() function.

    Parameters: 
        None

    Return: 
        string: Returns the user's valid input command.
    """
    while True:
        user_command = input(ENTER_COMMAND_MESSAGE)
        if check_input(user_command)== True:
            #end the loop only if theres a valid user command
            return user_command
            
def  add_piece(board: list[str], piece: str, column_index: int) -> bool:
    """
    Preconditions: the specified board will contain exactly 8 strings each with
    exactly 8 characters, represents a valid game state, the specified column index
    will be between 0 and 7 inclusive, the given piece will be exactly one character in length.

    Description: Add a piece to the specified column on the board.

    Parameters: 
        board: list[str]: Game board is represented a list of strings.
        piece: str: The specific game piece to add (either "X" or "O")
        column_index: int: Specific index of column, which the piece is to be added to.

    Return: 
        bool: Returns True if the piece was added successfully
              else returns false.
    """
    #transpose the column
    column_board= board[column_index]
    column_full_check = is_column_full(column_board)
    if column_full_check == True:
        print(FULL_COLUMN_MESSAGE)
        return False
    
    # Iterate through the string from right to left to find topmost available space
    for i in range(len(column_board) - 1, -1, -1):
        if column_board[i] == "-":
            #store the last empty space in the variable "i"
            last_occurrence = i
            break

    if last_occurrence != -1:
        # Replace the last occurrence of "-" with the piece
        new_column = column_board[:last_occurrence] + piece + column_board[last_occurrence + 1:]
        board[column_index] = new_column
        return True


def remove_piece(board: list[str], column_index: int) -> bool:
    """
    Description: Remove the upmost (highest) gamepiece from specified column on board.

    Preconditions: The specified board will contain exactly 8 strings each with
        exactly 8 characters, and represent a valid game state. 
        The specified column index must be between 0 and 7 inclusive.

    Parameters: 
        board: list[str]: The game board represented as a list of strings.
        column_index: int: The index of the column from which to remove the piece.

    Return: 
        bool: Returns True if the piece was successfully removed
            else return False.
    """
    column_board= board[column_index]
    #check if column is empty using the is_column_empty function
    column_empty_check = is_column_empty(column_board)
    if column_empty_check == True:
        print(EMPTY_COLUMN_MESSAGE)
        return False

    #create new column without the last piece
    new_column= "-" + column_board[:-1]
    board[column_index] = new_column
    return True

def check_win(board: list[str]) -> Optional[str]:
    """
    Description: Checks if theres a winner (on the board).

    Preconditions: The specified board will contain exactly 8 strings each with
        exactly 8 characters, all of which will be one of either X,O, or -. E

    Parameters: 
        board: list[str]: Game board is represented as a list of strings.

    Return: 
        Optional[str]: Return the piece of the winner/player (either "X" or "O")
            returns "-" for a tie (both win)
            returns None if no winner on board yet.
    """
    x_win=False
    o_win=False
    
    #check each column for horizontal win
    for column in range(8):
        column_check=""
        for row in board:
            #concacenate the character  at specified column index 
            column_check+=row[column]
        if "XXXX" in column_check:
            x_win= True
        elif "OOOO" in column_check:
            o_win=True
        
    for row in board:
        if "XXXX" in row:
            x_win=True
        elif "OOOO" in row:
            o_win=True
    
    #set range to where 4 pieces in a row is possible
    for i in range(len(board) - 3):
        for x in range(len(board[0]) - 3):
            # check diagonal win from top left to bottom right
            if board[i][x] == board[i+1][x+1] == board[i+2][x+2] == board[i+3][x+3]:
                if board[i][x] == 'X':
                    x_win=True
                elif board[i][x] == 'O':
                    o_win=True
            # check diagonal win from top right to bottom left
            if board[i][x+3] == board[i+1][x+2] == board[i+2][x+1] == board[i+3][x]:
                if board[i][x+3] == 'X':
                    x_win=True
                elif board[i][x+3] == 'O':
                    o_win=True
    #true and false cases for respective wins
    if x_win ==True and o_win==True:
        return "-"
    elif x_win==True:
        return "X"
    elif o_win ==True:
        return "O"
    else:
        return None

def play_game() -> None:
    """
    Description: Check if a player has won the game.

    Parameters: 
        board: list[str]: Game board is represented as strings in a list.

    Return: 
        Optional[str]: Return the winning player's piece ("X" or "O")
        return '-' on the occasion of a tie (both players win)
        return None if there is no winner on the board
    """
    current_player = "X"
    board = generate_initial_board()
    display_board(board)
    
    #Main game loop
    while True:
        if current_player == "X":
            print(PLAYER_1_MOVE_MESSAGE)
        else:
            print(PLAYER_2_MOVE_MESSAGE)
        piece = current_player
        
        # Help command case inside second loop so program does not prematurely exit
        while True:
            command = get_action()
            if command[0] in ["H", "h"]:
                print(HELP_MESSAGE)
                display_board(board)
                if current_player == "X":
                    print(PLAYER_1_MOVE_MESSAGE)
                else:
                    print(PLAYER_2_MOVE_MESSAGE)
                
                
            if command[0] in ['A', "a"]:
                column_index = int(command[1]) - 1
                if add_piece(board, piece, column_index):
                    break
            if command[0] in ["R", 'r']:
                column_index = int(command[1]) - 1
                if remove_piece(board, column_index):
                    break
            if command[0] in ["q", "Q"]:
                return  
        
        display_board(board)
        win = check_win(board)
        if win:
            if win == "X":
                print(PLAYER_1_VICTORY_MESSAGE)
                return
            elif win == "O":
                print(PLAYER_2_VICTORY_MESSAGE)
                return
            else:
                print(DRAW_MESSAGE)
                return
            break
        
        #change the player's turn
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        
    
if __name__ == "__main__":
    """
    Description: allows for the game to start automatically on start.
    Parameters: 
        None
    Return: 
        None
    """
    main()
