N = int(input())

ls = list(map(int, input().split()))
ls.sort()
print(ls[0], ls[-1])


