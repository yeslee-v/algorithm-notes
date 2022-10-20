from math import gcd

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(n * int(m / gcd(n, m)))
