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
