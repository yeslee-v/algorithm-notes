N = int(input());
ls = []

for i in range(N):
    ls.append(input())

for j in ls:
    ls_element = list(j)
    ls_count = [];
    count = 0
    for k in range(len(ls_element)):
        if ls_element[k] == 'O':
            count += 1
            ls_count.append(count)
        else:
            count = 0
            ls_count.append(count)

    print(sum(ls_count))