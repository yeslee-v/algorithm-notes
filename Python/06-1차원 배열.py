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

ls = []
for i in range(10):
    num = int(input()) % 42
    ls.append(num)

print(len(set(ls)))


#1546_평균

test = []; new_test = []
new_score = 0; count = 0
sum = 0; avg = 0

N = int(input())
test = list(map(int, input().split()))
max_score = max(test)

for i in range(len(test)):
    new_score = round((test[i]/max_score) * 100, 2)
    new_test.append(new_score)

for j in range(count):
    new_test.append(max_score)

for k in new_test:
    sum += k
    
print(round(sum/len(new_test), 6))
