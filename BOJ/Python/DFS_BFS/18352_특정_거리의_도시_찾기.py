import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n + 1)]
answer = []
visited = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)


BFS(x)

for i in range(n + 1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
