# 1)

ls_A = list(); ls_B = list()
A, B = map(int, input().split())

for i in str(A):
    ls_A.append(i)
ls_A.reverse()
a = ''.join(ls_A)

for j in str(B):
    ls_B.append(j)
ls_B.reverse()
b = ''.join(ls_B)

if a > b:
    print(a)
else:
    print(b)

# 2)
print(max([''.join(reversed(i)) for i in input().split()]))