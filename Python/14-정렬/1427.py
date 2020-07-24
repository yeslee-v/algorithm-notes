from sys import stdin

ls = []
for i in str(stdin.readline()):
      ls.append(i)
print(('').join(sorted(ls, reverse=True)))