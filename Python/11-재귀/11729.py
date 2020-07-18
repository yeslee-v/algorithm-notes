def hanoi(n, frm, to, other):
    if n == 1:
        move.append([frm, other])
    else:
        hanoi(n-1, frm, other, to)
        move.append([frm, other])
        hanoi(n-1, to, frm, other)

move = []   # 이동 경로를 담을 list
hanoi(int(input()), 1, 2, 3)    # play function

print(len(move))
print('\n'.join([' '.join(str(i) for i in j) for j in move]))