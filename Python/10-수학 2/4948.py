import math

result = []

while True:
    n = int(input())
    if n == 0:
        break
    result.append(n)

if 1 in result:
    result.remove(1)

for i in result:
    for j in range(2, math.ceil(math.sqrt(result[-1]))+1):

        print(i, j)