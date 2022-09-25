import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n

arr.sort()

for i in range(n):
    result = 0
    for j in range(i + 1):
        result += arr[j]
    answer[i] = result

print(sum(answer))
