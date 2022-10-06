import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0


def DFS(num):
    global cnt
    visited[num] = True
    for i in arr[num]:
        if not visited[i]:
            cnt += 1
            DFS(i)


for _ in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

DFS(1)
print(cnt)
