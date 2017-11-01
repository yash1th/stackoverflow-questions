n = 2
board = [[0] * 2 ** n for i in range(2 ** n)]
print(board)
rr = 1
rc = 1
currentNum=0

if n == 2:
    for i in range(len(board)):
        for j in board[i]:
            if board[rr + i][rc + j] == 0:
                board[rr + i][rc + j] = currentNum
    currentNum + 1