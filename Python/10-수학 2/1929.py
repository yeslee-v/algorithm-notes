import math


def isPrime(a):
    if 2 > a:
        return False
    elif a == 2:
        return True
    else:
        for b in range(2, math.ceil(math.sqrt(a)) + 1):
            if (a % b) == 0:
                return False
        return True


M, N = list(map(int, input().split()))

for i in range(M, N + 1):
    if isPrime(i):
        print(i)
