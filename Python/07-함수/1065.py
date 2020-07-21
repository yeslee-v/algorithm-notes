num = []
count = 0

N = int(input())

for i in range(1, N + 1):  # 입력받은 전체 수
    num.append(i)

for j in range(len(num)):  # 하나씩 끊기
    ls = []

    for k in str(num[j]):
        ls.append(k)

    if len(ls) <= 2:
        count += 1

    else:
        if int(ls[2]) - int(ls[1]) == int(ls[1]) - int(ls[0]):
            count += 1

print(count)