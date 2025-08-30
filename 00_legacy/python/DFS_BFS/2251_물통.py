from collections import deque

sender = [0, 0, 1, 1, 2, 2]     # 0 : A, 1 : B. 2 : C
receiver = [1, 2, 0, 2, 0, 1]
arr = list(map(int, input().split()))
visited = [[False for _ in range(201)] for _ in range(201)]
answer = [False] * 201


def BFS():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    answer[arr[2]] = True
    while queue:
        now = queue.popleft()
        a = now[0]
        b = now[1]
        c = arr[2] - (a + b)
        for i in range(6):
            next = [a, b, c]
            next[receiver[i]] += next[sender[i]]
            next[sender[i]] = 0
            if arr[receiver[i]] < next[receiver[i]]:
                next[sender[i]] = next[receiver[i]] - arr[receiver[i]]
                next[receiver[i]] = arr[receiver[i]]
            if not visited[next[0]][next[1]]:   # A, B의 물 양으로 visited 체크
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))
                if next[0] == 0:    # A가 0일 때 C 값을 저장한다
                    answer[next[2]] = True


BFS()

for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')
