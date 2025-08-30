arr = input().split('-')
result = 0


def operSum(n):
    res = 0
    tmp = str(n).split('+')
    for i in tmp:
        res += int(i)
    return res


for i in range(len(arr)):
    tmp = operSum(arr[i])
    if i == 0:
        result += tmp
    else:
        result -= tmp

print(result)
