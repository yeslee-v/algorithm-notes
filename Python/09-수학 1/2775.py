result = []
for i in range(int(input())):
    k = int(input()); n = int(input())
    ls = [i for i in range(1, n+1)]
    for f in range(k):
        for b in range(1, n):
            ls[b] += ls[b-1]
    result.append(ls[-1])

for i in result:
    print(i)