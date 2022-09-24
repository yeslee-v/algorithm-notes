import sys
input = sys.stdin.readline

n = int(input())
A = []

for i in range(n):
    A.append((int(input()), i))

sortedA = sorted(A)

max = 0

for i in range(n):
    if max < sortedA[i][1] - i: # i : 정렬 전 index
        max = sortedA[i][1] - i

print(max + 1) # A[1]부터 사용한다고 했으므로
