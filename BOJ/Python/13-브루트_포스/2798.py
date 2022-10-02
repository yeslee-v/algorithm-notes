from itertools import combinations

N, M = map(int, input().split())
ls = list(map(int, input().split()))

result = 0
for i in combinations(ls, 3):
    if sum(i) <= M:
        result = max(result, sum(i))

print(result)