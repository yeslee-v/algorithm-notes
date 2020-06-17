#10818_최소, 최대

N = int(input())

ls = list(map(int, input().split()))
ls.sort()
print(ls[0], ls[-1])


#2562_최댓값

ls = []
for i in range(9):
    ls.append(int(input()))
print(max(ls), ls.index(max(ls))+1)


#2577_숫자의 개수

ls = []; m_num = 1

for i in range(3):
    num = int(input())
    m_num *= num
ls = list(str(m_num))

for i in range(10):
    count = 0
    for j in range(len(ls)):
        if i == int(ls[j]):
            count += 1
    print(count)


#3052_나머지

ls = []; count = 0
for i in range(10):
    num = int(input())%42
    ls.append(num)
print(ls)
for j in range(10):
    for k in range(1, 10):
        print(ls[j], ls[k])
        






        
