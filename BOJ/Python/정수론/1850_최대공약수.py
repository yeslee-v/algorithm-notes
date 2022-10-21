import sys
from math import gcd

input = sys.stdin.readline

n, m = map(int, input().split())
# result = 1
gcd = gcd(n, m)
while gcd > 0:
    print(1, end='')
    gcd -= 1
    # result += pow(10, gcd) # 더하는 과정에서 시간 초과가 발생할 수 있다

# print(result)
