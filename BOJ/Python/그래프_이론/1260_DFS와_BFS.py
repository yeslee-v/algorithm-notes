from collections import deque

n, m, v = map(int, input().split())
arr = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

for i in range(n + 1):
    arr[i].sort() # 번호가 작은 노드부터 가기 위해 정렬


def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            DFS(i)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


DFS(v)
print()
visited = [False] * (n + 1)
BFS(v)
