# Prog-10: Tic-Tac-Toe
# 6330139021 ณพวุฒิ เจริญวิทย์วรกุล
# ผมขอยืนยันว่าเป็นผู้เขียนโปรมแกรมดังกล่าวด้วยตนเอง

import random
                     
def main():
    N = int(input('Board size = '))
    board = [["-"]*N for j in range(N)]
    end = False
    print_board(board)
    while(not end):
        print("========== Player Turn ==========")
        player_input(board)
        print_board(board)
        check = check_win(board)
        if(check != "-"):
            if(check == "D"):
                print("############# DRAW ##############")
            else:
                print("\\(^o^)/     YOU WIN !!!     \\(^o^)/")
            break
        print("======== Computer Turn ==========")
        com_fill(board)
        print_board(board)
        check = check_win(board)
        if(check != "-"):
            if(check == "D"):
                print("############# DRAW ##############")
            else:
                print("(;-;)    YOU LOSE!!!    (;-;)")
            break
    print("Game has ended, thanks for playing :D")

def com_fill(board):
    N = len(board)
    new_board = [[x for x in y] for y in board]
    for i in range(N):
        for j in range(N):
            if board[i][j] == "-":
                new_board[i][j] = "O"
                if(check_win(new_board) == "O"):
                    board[i][j] = "O"
                    return
                new_board[i][j] = "X"
                if(check_win(new_board) == "X"):
                    board[i][j] = "O"
                    return
                new_board[i][j] = "-"
    while True:
        i = random.randint(0, N-1)
        j = random.randint(0, N-1)
        if board[i][j] == "-":
            board[i][j] = "O"
            break

def print_board(board):
    N = len(board)
    print(" "*3 , end = "")
    for i in range(N):
        print((str(i)+ " "*(3))[:3], end = "")
    print()
    for row in range(N):
        print((str(row)+ " "*(3))[:3], end = "")
        for col in range(N):
            print(board[row][col], end = "    ")
        print()

def player_input(board):
    f = False
    while not f:
        try:
            row = int(input("row = "))
            col = int(input("col = "))
            f = fill(board, row, col)
            if (not f):
                print("!!! You can't fill that spot !!!")
                print("---try again---")
        except:
            print("!!! Invalid Input !!!")
            print("---try again---")

#------------------------------------------

def fill(board, r , c):
    if r >= len(board) or c >= len(board) or r < 0 or c < 0:
        return False
    if board[r][c] == "-":        
        board[r][c] = "X"
        return True

def check_win(board):
    def column(board):
        x = []
        for i in range(len(board)):
            y = []
            for j in range(len(board[i])):
                y.append(board[j][i])
            x.append(y)
        return x
    def cross(board):
        x = []
        y = []
        for i in range(len(board)):
            x.append(board[i][i])
            y.append(board[i][-i-1])
            
        return [x,y]
    iu = board + column(board) + cross(board)
    for i in range(len(iu)):
        if iu[i] == ["X"]*len(board):
            return "X"
        elif iu[i] == ["O"]*len(board):
            return "O"
    for i in range(len(iu)):
        if not("X" in iu[i] and "O" in iu[i]):
            break
    else:
        return "D"
    return "-"

#------------------------------------------

main()