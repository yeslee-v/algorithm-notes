N = int(input())
num = list(map(int, input().split()))
result = 0

if len(num) == N:
    for i in num:
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:  # 1 1, 3 1, 3 2, 3 3, 5 1, 5 2, 5 3..
                cnt += 1
        if cnt == 2:
            result += 1

print(result)