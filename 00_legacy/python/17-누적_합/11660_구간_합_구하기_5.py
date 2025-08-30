import sys

input = sys.stdin.readline
n, m = map(int, input().split())
origin = [[0] * (n + 1)]
sum_arr = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
  origin_row = [0] + [int(x) for x in input().split()]
  origin.append(origin_row)
  
# fill interval sum
for i in range(1, n + 1):
  for j in range(1, n + 1):
    sum_arr[i][j] = sum_arr[i][j - 1] + sum_arr[i - 1][j] - sum_arr[i - 1][j - 1] + origin[i][j]

# calculate
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  result = sum_arr[x2][y2] - sum_arr[x1 - 1][y2] - sum_arr[x2][y1 - 1] + sum_arr[x1 - 1][y1 - 1]
  print(result)
