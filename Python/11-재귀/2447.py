def stars(n):
    ls = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            ls.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            ls.append(n[i % len(n)] * 3)

    return ls


star = ["***", "* *", "***"]
n = int(input())
k = 0

while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)

for i in star:
    print(i)

# another

i = 1
N = int(input())
ls = ['*']

while i < N:
    ls2 = []
    ls3 = []

    for a in ls:
        ls2.append(a * 3)
        ls3.append(a + ' ' * i + a)

    ls = ls2 + ls3 + ls2
    i *= 3

for a in list:
    print(a)
