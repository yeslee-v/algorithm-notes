from sys import stdin

i = 2
N = int(stdin.readline())
while N > 1:
    if N % i == 0:
        print(i)
        N = N // i
    else:
        i += 1