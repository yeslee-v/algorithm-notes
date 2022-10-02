import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0] * n   # cumulative sum
comb = [0] * m      # same remainder count
sum_arr[0] = arr[0]
result = 0

for i in range(1, n):
    sum_arr[i] = sum_arr[i - 1] + arr[i]

for i in range(n):
    remainder = sum_arr[i] % m
    if not remainder:
        result += 1
    comb[remainder] += 1

for i in range(m):
    if comb[i] > 1:
        result += (comb[i] * (comb[i] - 1) // 2)

print(result)
