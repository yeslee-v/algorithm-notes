import math

n, m = map(int, input().split())
arr = [0] * (m + 1)

for i in range(2, m + 1):
    arr[i] = i

for i in range(2, int(math.sqrt(m) + 1)):
    if not arr[i]:
        continue
    for j in range(i + i, m + 1, i):
        arr[j] = 0

for i in range(n, m + 1):
    if arr[i]:
        print(arr[i])
