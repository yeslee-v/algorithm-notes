m = int(input())
n = 0
for i in range(m + 1):
    arr = list(map(int, str(i)))
    n = i + sum(arr)
    if n == m:
        print(i)
        break

    if i == m:
        print(0)
