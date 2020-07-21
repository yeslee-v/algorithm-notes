C = int(input())

for i in range(C):
    score = list(map(int, input().split()))
    avg = (sum(score) - score[0]) / (len(score) - 1)
    count = 0;

    for j in range(score[0]):
        if score[j + 1] > avg:
            count += 1

    upper_ratio = count * 100 / (len(score) - 1)
    print("%.3f%%" % upper_ratio)