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