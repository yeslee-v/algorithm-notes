import math

n, m = map(int, input().split())
arr = [0] * 10000001
cnt = 0

for i in range(2, len(arr)):
    arr[i] = i

for i in range(2, int(math.sqrt(len(arr))) + 1):
    if arr[i] == 0:
        continue
    for j in range(i + i, len(arr), i):
        arr[j] = 0

for i in range(2, 10000001):
    if arr[i] != 0:
        tmp = arr[i]
        while arr[i] <= m / tmp:
            if arr[i] >= n / tmp:
                cnt += 1
            tmp = tmp * arr[i]

print(cnt)
