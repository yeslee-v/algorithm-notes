self_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i = i + int(j)
    generated_num.add(i)
self_num = self_num - generated_num

for k in sorted(self_num):
    print(k)