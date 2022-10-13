n = int(input())
timeTable = []
cnt = 0
end = -1

for _ in range(n):
    timeTable.append(list(map(int, input().split())))

# 종료 시간이 동일한 경우, 시작 시간이
timeTable = sorted(timeTable, key=lambda t: t[0])
timeTable = sorted(timeTable, key=lambda t: t[1])

for i in range(n):
    if timeTable[i][0] >= end:
        end = timeTable[i][1]
        cnt += 1

print(cnt)
