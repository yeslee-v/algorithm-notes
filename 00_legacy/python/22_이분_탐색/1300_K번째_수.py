n = int(input())
k = int(input())

start = 1
end = k
result = 0
while start <= end:
    mid = int((start + end) / 2)
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(int(mid / i), n) # int(mid / i)와 n 중 작은 값이 cnt에 더해진다
    if cnt < k:
        start = mid + 1
    elif k <= cnt:
        result = mid
        end = mid - 1

print(result)
