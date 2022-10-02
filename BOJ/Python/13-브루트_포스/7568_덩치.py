n = int(input())
arr = []
rank = []

for i in range(n):
    m = input().split(' ')
    arr.append(list(map(int, m)))

for i in range(n):
    rank.append(1)

i = 0
while (i < n):
    j = 0
    while (j < n):
        if (arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]):
            rank[i] += 1
        j += 1
    i += 1

for i in rank:
    if i != rank[-1]:
        print(i, end=' ')
    else:
        print(i)