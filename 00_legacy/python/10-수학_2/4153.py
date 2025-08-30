import math

ls_all = []

while True:
    ls_input = list(map(int, input().split()))
    ls_input.sort()
    if ls_input == [0, 0, 0]:
        break
    else:
        ls_all.append(ls_input)

for i in range(len(ls_all)):
    if ls_all[i][2] == math.sqrt((ls_all[i][0] ** 2) + (ls_all[i][1] ** 2)):
        print("right")
    else:
        print("wrong")