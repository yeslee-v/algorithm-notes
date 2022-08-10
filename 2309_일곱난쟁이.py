def seven_dwarf(idx, cnt, weight, dwarf_arr, answer):
    if idx >= len(answer): return
    if weight == 100: return
    seven_dwarf(idx, cnt, weight, dwarf_arr, answer)
    answer.pop(dwarf_arr[idx])
    seven_dwarf(idx + 1, cnt, weight + dwarf_arr[idx], dwarf_arr, answer.append(dwarf_arr[idx]))
    
dwarf_arr = []
answer = []
for i in range(9):
    dwarf_arr.append(int(input()))
dwarf_arr.sort()

seven_dwarf(0, 0, 0, dwarf_arr, answer)
for i in answer:
    print(i)