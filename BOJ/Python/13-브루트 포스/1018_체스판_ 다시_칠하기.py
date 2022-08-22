n, m = list(map(int, input().split(' ')))
board = []
res = []

for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        idx_w = 0
        idx_b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        idx_w += 1
                    if board[k][l] != 'B':
                        idx_b += 1
                else:
                    if board[k][l] != 'B':
                        idx_w += 1
                    if board[k][l] != 'W':
                        idx_b += 1
        res.append(min(idx_w, idx_b))

print(min(res))