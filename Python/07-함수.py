# 15596_정수 N개의 합

def solve(n):
    return sum(n)


# 4673_셀프 넘버

self_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i = i + int(j)
    generated_num.add(i)
self_num = self_num - generated_num

for k in sorted(self_num):
    print(k)


# 1065_한수

num = []; count = 0

N = int(input())

for i in range(1,N+1):      # 입력받은 전체 수
    num.append(i)

for j in range(len(num)):       # 하나씩 끊기
    ls = []
    
    for k in str(num[j]):
        ls.append(k)
        
    if len(ls) <=2:
        count +=1
        
    else:
        if int(ls[2]) - int(ls[1]) == int(ls[1]) - int(ls[0]):
            count += 1

print(count)    


