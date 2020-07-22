from sys import stdin

result = []
for i in range(int(stdin.readline())):
    result.append(int(stdin.readline()))

for i in sorted(result):
    print(i)