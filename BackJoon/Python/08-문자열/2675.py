T = int(input())
case = []

for i in range(T):
    R = input().split()
    case.append(R)

for m in range(T):
    answer = []
    for i in str(case[m][1]):
        for j in range(1, int(case[m][0]) + 1):
            result = i * j
        answer.append(result)

    print(''.join(answer))