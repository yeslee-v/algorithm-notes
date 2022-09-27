import sys

input = sys.stdin.readline


def merge_sort(start, end):
    global result
    if end - start < 1:
        return
    mid = int(start + (end - start) / 2)
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    for i in range(start, end + 1):
        tmp[i] = arr[i]
    k = start
    idx1 = start
    idx2 = mid + 1
    while idx1 <= mid and idx2 <= end:
        if tmp[idx1] > tmp[idx2]:
            arr[k] = tmp[idx2]
            result = result + idx2 - k
            k += 1
            idx2 += 1
        else:
            arr[k] = tmp[idx1]
            k += 1
            idx1 += 1
    while idx1 <= mid:
        arr[k] = tmp[idx1]
        k += 1
        idx1 += 1
    while idx2 <= end:
        arr[k] = tmp[idx2]
        k += 1
        idx2 += 1


n = int(input())
arr = list(map(int, input().split()))
result = 0
arr.insert(0, 0)    # index 맞추려고 0번째 index에 0을 넣는다
tmp = [0] * int(n + 1)

merge_sort(1, n)

print(result)
