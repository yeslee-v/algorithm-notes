from math import factorial

t = int(input())


def Comb(n, m):
    comb = 1
    for k in range(n):
        comb *= (m - k)
    div = factorial(n)
    result = comb // div
    return result


for i in range(t):
    n, m = map(int, input().split())
    print(Comb(n, m))
