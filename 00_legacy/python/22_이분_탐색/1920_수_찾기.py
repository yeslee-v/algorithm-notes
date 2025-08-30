import sys

input = sys.stdin.readline

n = int(input())
n_arr = sorted(list(map(int, input().split())))

m = int(input())
m_arr = list(map(int, input().split()))

for i in range(m):
    find = False
    now = m_arr[i]
    # binary search
    start = 0
    end = len(n_arr) - 1
    while start <= end:
        mid_idx = int((start + end) / 2)
        mid_value = n_arr[mid_idx]
        if now < mid_value:
            end = mid_idx - 1
        elif mid_value < now:
            start = mid_idx + 1
        else:
            find = True
            break
    print(1 if find else 0)
