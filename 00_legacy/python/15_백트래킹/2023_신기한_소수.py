import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())


def isPrime(m):
    for i in range(2, int(m / 2 + 1)):
        if not m % i:
           return False
    return True


def DFS(m):
    if len(str(m)) == n:
        print(m)
    else:
        for i in range(1, 10):
            if not i % 2:
                continue
            if isPrime(m * 10 + i):
                DFS(m * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)
