from queue import PriorityQueue

positivePq = PriorityQueue()
negativePq = PriorityQueue()
n = int(input())
oneCnt = 0
zeroCnt = 0
result = 0

for _ in range(n):
    num = int(input())
    if num == 0:
        zeroCnt += 1
    elif num == 1:
        oneCnt += 1
    elif num > 1:
        positivePq.put(num * -1) # 내림차순 정렬을 위해 -1을 곱한다
    else:
        negativePq.put(num)

while positivePq.qsize() > 1:
    first = positivePq.get() * -1
    second = positivePq.get() * -1
    result += first * second

if positivePq.qsize() != 0:
    result += positivePq.get() * -1

while negativePq.qsize() > 1:
    first = negativePq.get()
    second = negativePq.get()
    result += first * second

if negativePq.qsize() != 0:
    if not zeroCnt: # 0이 없을 때만 더한다, 있으면 0을 곱해 음수를 0으로 상쇄시킨다
        result += negativePq.get()

result += oneCnt
print(result)
