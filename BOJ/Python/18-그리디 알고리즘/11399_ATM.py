n = int(input())
arr = list(map(int, input().split()))
result = [0] * n
answer = 0

for i in range(1, n):
    insert_point = i
    insert_value = arr[i]
    for j in range(i - 1, -1, -1):
        if arr[j] < arr[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        arr[j] = arr[j - 1]
    arr[insert_point] = insert_value

result[0] = arr[0]

for i in range(1, n):
    result[i] = result[i - 1] + arr[i]

for i in range(n):
    answer += result[i]

print(answer)
