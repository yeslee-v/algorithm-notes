from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                queue.append(i)


for i in range(1, n + 1):
    visited = [False] * (n + 1) # 단방향으로 신뢰하므로 모든 index를 다 돌아야한다.
    BFS(i)

standard = 0
for i in range(1, n + 1):
    standard = max(standard, answer[i])

for i in range(1, n + 1):
    if standard == answer[i]:
        print(i, end=' ')
