from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
myQueue = PriorityQueue()

for i in range(n):
    num = int(input())
    if num == 0:
        if myQueue.empty():
            print('0\n')
        else:
            tmp = myQueue.get()
            print(str(tmp[1])+'\n')
    else:
        myQueue.put((abs(num), num))
