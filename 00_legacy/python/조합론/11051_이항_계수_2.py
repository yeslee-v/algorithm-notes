import sys
from math import factorial

input = sys.stdin.readline
n, m = map(int, input().split())
result = 1

for i in range(m):
    result *= (n - i)

mp = factorial(m)
print((result // mp) % 10007)   # int()의 정밀도: 15자리, 문제의 정밀도(1000!): 2500자리
