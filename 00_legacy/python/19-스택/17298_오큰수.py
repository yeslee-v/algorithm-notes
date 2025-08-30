n = int(input())
arr = list(map(int, input().split()))
idxArr = [0] * n # 값이 아닌 index를 넣는다
myStack = []

for i in range(n):
    while myStack and arr[myStack[-1]] < arr[i]: # 2 5
        idxArr[myStack.pop()] = arr[i]
    myStack.append(i)

while myStack:
    idxArr[myStack.pop()] = -1

result = ""

for i in range(n):
    result += str(idxArr[i]) + " "

print(result)
