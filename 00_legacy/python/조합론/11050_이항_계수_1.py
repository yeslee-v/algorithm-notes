n, k = map(int, input().split())

answer = 1
for i in range(1, k + 1):
    answer *= (n - i + 1) / i

print(int(answer))
