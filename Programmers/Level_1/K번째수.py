def solution(array, commands):
  slice_arr = []
  picked_arr = []
  
  for i in commands:
    slice_arr = array[i[0] - 1:i[1]]
    slice_arr.sort()
    picked_arr.append(slice_arr[i[2] - 1])
    
  return picked_arr

answer = solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(answer)