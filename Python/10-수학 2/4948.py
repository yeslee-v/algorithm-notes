raw = []
result = []


def isPrime(a):
    if 2 > a:
        return False
    for b in range(2, a):
        if (a % b) == 0:
            return False
    return True


while True:
    n = int(input())
    if n == 0:
        break
    raw.append(n)

for i in range(len(raw)):
    result.append([])
    for j in range((raw[i] + 1), (2 * raw[i]) + 1):
        if isPrime(j):
            result[i].append(j)

for i in range(len(result)):
    print(len(result[i]))
