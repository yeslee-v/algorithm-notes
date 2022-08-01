test = []
new_test = []
new_score = 0
count = 0
sum = 0
avg = 0

N = int(input())
test = list(map(int, input().split()))
max_score = max(test)

for i in range(len(test)):
    new_score = round((test[i] / max_score) * 100, 2)
    new_test.append(new_score)

for j in range(count):
    new_test.append(max_score)

for k in new_test:
    sum += k

print(round(sum / len(new_test), 6))