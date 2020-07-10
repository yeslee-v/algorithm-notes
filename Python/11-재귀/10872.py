result = 1

N = int(input())

for i in range(1, N+1):
    result *= i

print(result)

# recursive function

def func(n):
    return int(n <= 1) or n * func(n - 1)


print(func(int(input())))
