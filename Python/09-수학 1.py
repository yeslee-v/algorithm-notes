# 1712_손익 분기점

import timeit

start = timeit.default_timer()

A, B, C = map(int, input().split())

if B < C:
    count = int(A/(C-B))
    print(count+1)
else:
    print(-1)

end = timeit.default_timer()
print(end-start)


# 2839_설탕 배달

N = int(input())
num_pack = 0

while N > 0:
    if N % 5 != 0:
        N -= 3
        if N < 0:
            num_pack = -1
            break
        num_pack += 1
    elif N % 5 == 0:
        num_pack += 1
        N -= 5
    elif N % 5 != 0 and N % 3 != 0:
        num_pack = -1

print(num_pack)