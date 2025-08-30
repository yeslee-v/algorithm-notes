from collections import deque

v = int(input())
arr = [[] for _ in range(v + 1)]
distance = [0] * (v + 1)
result = 1
visited = [False] * (v + 1)

for _ in range(v):
    tmp = list(map(int, input().split()))
    s = tmp[0] # arr의 index와 동일하다
    j = 0
    while tmp[j] != -1:
        if j % 2 and tmp[j + 1] != -1:
            arr[s].append((tmp[j], tmp[j + 1]))
        j += 1


def BFS(v):
    global distance
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


BFS(result)


for i in range(2, v + 1):
    result = i if distance[result] < distance[i] else result

# 긴 거리에서 너비 우선 탐색을 하기 때문에 거리 리스트와 방문 리스트 초기화
distance = [0] * (v + 1)
visited = [False] * (v + 1)


# update된 result로 탐색
BFS(result)
print(max(distance))
