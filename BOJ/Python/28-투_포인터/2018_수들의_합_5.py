n = int(input())

cnt = 1
start_idx = 1
end_idx = 1
result = 1

while end_idx != n:
    if result == n:
        cnt += 1
        end_idx += 1
        result += end_idx
    elif result > n:
        result -= start_idx
        start_idx += 1
    elif result < n:
        end_idx += 1
        result += end_idx

print(cnt)


