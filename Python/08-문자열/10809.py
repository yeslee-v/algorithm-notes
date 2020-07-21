S = input(); ls = []

for i in S:
    ls.append(i)

for m in range(ord('a'), ord('z') + 1):
    if chr(m) in ls:
        print(ls.index(chr(m)))
    else:
        print(-1)