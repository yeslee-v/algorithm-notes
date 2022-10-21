from math import gcd

n = int(input())
arr = [[] for _ in range(n)]
visited = [False] * n
value = [0] * n
lcm = 1


def DFS(v):
    visited[v] = True
    for i in arr[v]:
        next = i[0]
        if not visited[next]:
            value[next] = value[v] * i[2] // i[1] # 질량의 비율을 곱한다
            DFS(next)


for _ in range(n - 1):
    a, b, p, q = map(int, input().split())
    arr[a].append((b, p, q))
    arr[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

value[0] = lcm
DFS(0)
mgcd = value[0]

for i in range(1, n):
    mgcd = gcd(mgcd, value[i])

for i in range(n):
    print(int(value[i] // mgcd), end=' ')
