import math

min, max = map(int, input().split())
arr = [False] * (max - min + 1)
cnt = 0

for i in range(2, int(math.sqrt(max) + 1)):
    num = pow(i, 2)
    start = int(min / num)
    if min % num:
        start += 1
    for j in range(start, int(max / num) + 1):
        arr[int((j * num) - min)] = True

for i in range(0, max - min + 1):
    if not arr[i]:
        cnt += 1

print(cnt)
