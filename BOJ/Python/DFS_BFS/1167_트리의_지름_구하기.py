from collections import deque

v = int(input())
arr = [[] for _ in range(v + 1)]


for _ in range(v):
    data = list(map(int, input().split()))
    idx = 0
    S = data[idx]
    idx += 1
    while True:
        if data[idx] == -1:
            break
        arr[S].append((data[idx], data[idx + 1]))
        idx += 2

distance = [0] * (v + 1)
visited = [False] * (v + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now] + i[1]


BFS(1)
result = 1

for i in range(2, v + 1):
    if distance[result] < distance[i]:
        result = i

distance = [0] * (v + 1)
visited = [False] * (v + 1)
BFS(result)
distance.sort()
print(distance[v])
