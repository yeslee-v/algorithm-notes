m = int(input())
d = list(map(int, input().split()))
prob = [0] * len(d)
k = int(input())
t = 0
answer = 0

for i in range(0, m):
    t += d[i]

for i in range(0, m):
    if k <= d[i]:
        prob[i] = 1
        for j in range(0, k):
            prob[i] = prob[i] * (d[i] - j) / (t - j)
        answer += prob[i]

print(answer)
