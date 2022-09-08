n = int(input())
cnt = 0
shun = 666

while True:
    if '666' in str(shun):
        cnt += 1
    if n == cnt:
        print(shun)
        break
    shun += 1