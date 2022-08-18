def solution():
    a = []
    for i in range(9):
        a.append(int(input()))
    res = sum(a)

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if res - (a[i] + a[j]) == 100:
                a.pop(j)
                a.pop(i)
                a.sort()
                return a

a = solution()
for i in a:
    print(i)
