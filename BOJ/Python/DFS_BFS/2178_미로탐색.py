# coding=utf-8
from collections import deque

# 상하좌우 탐색
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]


# 갈 수 있는 너비를 먼저 탐색한 후 다음 깊이로 넘거가기 때문에 DFS보다 BFS가 적합하다
def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if -1 < x < n and -1 < y < m:
                if arr[x][y] == 1 and not visited[x][y]:
                    visited[x][y] = True
                    arr[x][y] = arr[now[0]][now[1]] + 1
                    queue.append((x, y))


for i in range(n):
    arr[i] = list(input())
    for j in range(m):
        arr[i][j] = int(arr[i][j])

BFS(0, 0)
print(arr[n - 1][m - 1])
