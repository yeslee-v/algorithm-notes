from queue import PriorityQueue

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    pq.put(int(input()))

d1 = 0
d2 = 0
answer = 0

while pq.qsize() > 1:
    d1 = pq.get()
    d2 = pq.get()
    tmp = d1 + d2
    answer += tmp
    pq.put(tmp)

print(answer)
