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