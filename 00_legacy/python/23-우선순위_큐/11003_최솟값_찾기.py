from collections import deque
n, l = map(int, input().split())
a = list(map(int, input().split()))
myDeque = deque()

for i in range(n):
    while myDeque and myDeque[-1][0] > a[i]:
        myDeque.pop()
    myDeque.append((a[i], i))
    if myDeque[0][1] <= i - l:
        myDeque.popleft()
    print(myDeque[0][0], end=' ')
