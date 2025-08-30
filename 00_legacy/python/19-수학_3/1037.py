from sys import stdin
N = int(input())

ls = sorted(list(map(int, stdin.readline().split())))
print(ls[0]*ls[-1])

# or

ls = list(map(int, stdin.readline().split()))
print(max(ls) * min(ls))
