import math
import timeit

start = timeit.default_timer()

sieve = []
M, N = map(int, input().split())

for i in range(M, N + 1):
    sieve.append(i)

if 1 in sieve:
    sieve.remove(1)

for j in range(2, math.ceil(math.sqrt(sieve[-1]))):
    for k in sieve:
        if k / j == 1:
            pass
        elif j < k:
            if k % j == 0:
                sieve.remove(k)

for answer in sieve:
    print(answer)

end = timeit.default_timer()

print("time : ", end - start)
