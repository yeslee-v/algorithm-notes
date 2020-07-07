import math

num = []
result = 0
M = int(input())
N = int(input())

if M <= N:
    for i in range(M, N + 1):
        num.append(i)
    if 1 in num:  # 리스트 안에 1이 있는 경우
        num.remove(1)

for i in range(2, math.ceil(math.sqrt(10000))):
    for j in num:
        if j / i == 1:  # 같은 숫자는 패스
            pass
        elif j % i == 0:
            num.remove(j)

if not num:  # 리스트가 비었을 때
    print("-1")
else:
    for k in num:
        result += k
    print(result)
    print(num[0])
