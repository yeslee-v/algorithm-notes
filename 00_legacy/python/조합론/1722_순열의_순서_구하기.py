n = int(input())
arr = list(map(int, input().split()))
visited = [False] * (n + 1)
S = [0] * (n + 1)
F = [0] * (n + 1)
F[0] = 1

for i in range(1, n + 1):
    F[i] = F[i - 1] + 1

if arr[0] == 1:
    k = arr[1]
    for i in range(1, n + 1):
        cnt = 1
        for j in range(1, n + 1):
            if visited[j]:
                continue
            if k <= (cnt * F[n - i]):
                k -= (cnt - 1) * F[n - i]
                S[i] = j
                visited[j] = True
                break
            cnt += 1
    for i in range(1, n + 1):
        print(S[i], end=' ')
else:
    k = 1
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, arr[i]):
            if not visited[j]:
                cnt += 1
        k += cnt * F[n - i]
        visited[arr[i]] = True
    print(k)
