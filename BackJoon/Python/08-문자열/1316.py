N = int(input()); result = 0

for i in range(N):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)