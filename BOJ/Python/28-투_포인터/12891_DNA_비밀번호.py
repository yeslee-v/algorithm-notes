checkList = [0] * 4
myList = [0] * 4
checkSecret = 0


def myAdd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    if c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    if c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    if c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1


def myRemove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    if c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    if c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    if c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1


s, p = map(int, input().split())
dna = list(input())
checkList = list(map(int, input().split()))
result = 0

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(p):
    myAdd(dna[i])

if checkSecret == 4:
    result += 1

for i in range(p, s):
    j = i - p
    myAdd(dna[i])
    myRemove(dna[j])
    if checkSecret == 4:
        result += 1

print(result)
