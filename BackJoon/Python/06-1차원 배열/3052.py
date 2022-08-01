ls = []
for i in range(10):
    num = int(input()) % 42
    ls.append(num)

print(len(set(ls)))
