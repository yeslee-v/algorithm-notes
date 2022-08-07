def solution(sizes):
  max_array = []
  min_array = []
  
  for i in sizes:
    max_array.append(i[1]) if i[1] > i[0] else max_array.append(i[0])
    min_array.append(i[0]) if i[1] > i[0] else min_array.append(i[1])
    
  return max(max_array) * max(min_array)

answer1 = solution([[60, 50], [30, 70], [60, 30], [80, 40]])
answer2 = solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
answer3 = solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])

print(answer1)
print(answer2)
print(answer3)