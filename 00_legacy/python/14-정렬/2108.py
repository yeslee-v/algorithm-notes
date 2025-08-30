from sys import stdin
from collections import Counter

ls = []
for i in range(int(stdin.readline())):
    ls.append(int(stdin.readline()))


def num_avg(n):
    return round(sum(n) / len(n))


def num_median(n):
    n.sort()
    return n[len(n) // 2]


def num_counter(n):
    counter = Counter(n).most_common()

    if len(n) > 1:
        if counter[0][1] == counter[1][1]:  # counter[0][1]: 가장 큰 최빈값의 빈도수
            result = counter[1][0]
        else:
            result = counter[0][0]
    else:
        result = counter[0][0]

    return result


def num_range(n):
    return max(n) - min(n)


print(num_avg(ls))
print(num_median(ls))
print(num_counter(ls))
print(num_range(ls))
