import math

n = int(input())
arr = [0] * 10000001

for i in range(2, len(arr)):
    arr[i] = i

for j in range(2, int(math.sqrt(len(arr)) + 1)):
    if arr[j] == 0:
        continue
    for k in range(j + j, len(arr), j):
        arr[k] = 0


def isPalindrome(target):
    tmp = list(str(target))
    s = 0
    e = len(tmp) - 1
    while s < e:
        if tmp[s] != tmp[e]:
            return False
        s += 1
        e -= 1
    return True


num = n

while True:
    if arr[num]:
        if isPalindrome(arr[num]):
            print(arr[num])
            break
    num += 1
