# 11654_아스키 코드

n = input()
print(ord(n))


# 11720_숫자의 합

N = int(input()); num = int(input())
answer = 0

for i in str(num):
    answer += int(i)
print(answer)


# 10809_알파벳 찾기

S = input(); ls = []

for i in S:
    ls.append(i)

for m in range(ord('a'), ord('z') + 1):
    if chr(m) in ls:
        print(ls.index(chr(m)))
    else:
        print(-1)


# 2675_문자열 반복

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