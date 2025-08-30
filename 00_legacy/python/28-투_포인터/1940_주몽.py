import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

start_idx = 0
end_idx = n - 1
cnt = 0

while start_idx < end_idx:
    if arr[start_idx] + arr[end_idx] == m:
        cnt += 1
        start_idx += 1
        end_idx -= 1
    elif arr[start_idx] + arr[end_idx] < m:
        start_idx += 1
    else:
        end_idx -= 1

print(cnt)
