"""each player chooses a location for his mark"""
"""
 ask player one for the coordinates
 if the cell is empty place the right mark in the right cell
 if the cell is full ask the player again
 print the board after every move
 ask player two fo the coordinates
 do everything again
 do it till the board is full
"""
game_board = [['-', '-', '-'],
              ['-', '-', '-'],
              ['-', '-', '-']]


def is_room_left(game_board):
    for line in game_board:
        for cell in line:
            if cell == '-':
                return True
    return False


# TODO: need to check if the input is int and in range

while is_room_left(game_board):
    while True:
        row_one = int(input("enter the row for the x "))
        column_one = int(input("enter the column for the x "))
        if game_board[row_one][column_one] == '-':
            break
        print("this cell is full, please try again")
    game_board[row_one][column_one] = 'x'
#    row_one = int(input("enter the row for the x "))
#    column_one = int(input("enter the column for the x "))
#    while game_board[row_one][column_one] != '-':
#        print("this cell is full, please try again")
#        row_one = int(input("enter the row for the x "))
#        column_one = int(input("enter the column for the x "))
#    game_board[row_one][column_one] = 'x'
    for line in game_board:
        print(line)
    if not is_room_left(game_board):
        break
    while True:
        row_two = int(input("enter the row for the 0 "))
        column_two = int(input("enter the column for the 0 "))
        if game_board[row_two][column_two] == '-':
            break
        print("this cell is full, please try again")
#    row_two = int(input("enter the row for the 0 "))
#    column_two = int(input("enter the column for the 0 "))
#    while game_board[row_two][column_two] != '-':
#        print("this cell is full, please try again")
#        row_two = int(input("enter the row for the 0 "))
#        column_two = int(input("enter the column for the 0 "))
#    game_board[row_two][column_two] = '0'
    for line in game_board:
        print(line)
