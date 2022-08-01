ls = []
for i in range(9):
    ls.append(int(input()))
print(max(ls), ls.index(max(ls))+1)