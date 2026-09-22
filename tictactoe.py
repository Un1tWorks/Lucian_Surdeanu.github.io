board = [ 1, 2, 3,
          4, 5, 6,
          7, 8, 9 ]

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    
print_board(board)

def player1():
    position=input("pick a position from the board 1-9, Player 1 entered:")
    
    try:
        position = int(position)
    except ValueError:
        print_board(board)
        print("any charachter that isn't a integer number, is not accepted, try again")
        return player1()
        #position=int(input("please type a number from 1-9, Player 1 entered: "))
    
    if position < 1 or position > 9:
        print_board(board)
        print("the number has to be between 1 and 9, not lower, not higher, try again")
        return player1()
        
    position -= 1

    if isinstance(board[position], int) == True:
        board[position] = "X"
    else:
        print_board(board)
        print("that slot is occupied, try again")
        return player1()
    
    print_board(board)
    
def player2():
    position=input("pick a position from the board 1-9, Player 2 entered:")
    
    try:
        position = int(position)
    except ValueError:
        print_board(board)
        print("any charachter that isn't a integer number, is not accepted, try again")
        return player2()
    
    if position < 1 or position > 9:
        print_board(board)
        print("the number has to be between 1 and 9, not lower, not higher, try again")
        return player2()
        
    position -= 1

    if isinstance(board[position], int) == True:
        board[position] = "O"
    else:
        print_board(board)
        print("that slot is occupied, try again")
        return player2()
        
    print_board(board)      

symbol = "X"
x = 0

#combos = ( (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))

def winning_combos():
    cnt = 1
    global x
    while cnt < 3:
        if cnt == 1:
            symbol = "X"
        if cnt == 2:
            symbol = "O"
        if board[0] == symbol and board[1] == symbol and board[2] == symbol:
            print(f"player {cnt} won")
            x=1
        elif board[3] == symbol and board[4] == symbol and board[5] == symbol:
            print(f"player {cnt} won")
            x=1
        elif board[6] == symbol and board[7] == symbol and board[8] == symbol:
            print(f"player {cnt} won")
            x=1
        elif board[0] == symbol and board[4] == symbol and board[8] == symbol:
            print(f"player {cnt} won")
            x=1
        elif board[2] == symbol and board[4] == symbol and board[6] == symbol:
            print(f"player {cnt} won")
            x=1
        elif board[0] == symbol and board[3] == symbol and board[6] == symbol:
            print(f"player {cnt} won")
            x=1
        elif board[1] == symbol and board[4] == symbol and board[7] == symbol:
            print(f"player {cnt} won")
            x=1
        elif board[2] == symbol and board[5] == symbol and board[8] == symbol:
            print(f"player {cnt} won")
            x=1
        cnt += 1
counter = 0  
while x == 0:
    if counter % 2 == 0:
        player1()
        symbol = 1
    elif counter % 2 == 1:
        player2()
        symbol = 2
    counter += 1
    winning_combos()
    if counter == 9 and x != 1:
        print("it's a draw!")
        x = 1