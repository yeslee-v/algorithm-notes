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


# Using Sieve of Eratosthenes

import math

N = int(input())
num = list(map(int, input().split()))
num_all = list(range(2, 1001))
cnt = 0

if len(num) == N:
    for i in range(2, math.ceil(math.sqrt(1000))):  # math.ceil: 반올림 / math.sqrt: 제곱근
        for j in num_all:
            if j / i == 1:  # 같은 숫자는 패스
                pass
            elif j % i == 0:    # 그 외에도 나뉘는 수가 있으면 제거
                num_all.remove(j)

for k in num:
    if k in num_all:
        cnt += 1

print(cnt)