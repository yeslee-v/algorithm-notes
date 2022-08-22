n, m = list(map(int, input().split(' ')))
board = []
i = 0
res = 0

while (i < n):
    board.append(input())
    i += 1

for i in range(len(board) - 2):
    for j in range(len(board) - 2):
        if board[i][j] == board[i][j + 1] and board[i][j] != board[i][j + 2]:
            res += 1
    if board[i][j] == board[i + 1][j] and board[i][j] == board[i + 2][j]:
        res += 1

print(res)