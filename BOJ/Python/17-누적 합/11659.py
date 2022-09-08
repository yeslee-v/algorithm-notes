import sys

input = sys.stdin.readline

n, m = map(int, input().split( ))
arr = list(map(int, input().split( ))) 

sum_arr = [0] * (n + 1)

for i in range(len(arr)):
  sum_arr[i + 1] = sum_arr[i] + arr[i]
    
for _ in range(m):
  i, j = map(int, input().split( ))
  print(sum_arr[j] - sum_arr[i - 1]) 
