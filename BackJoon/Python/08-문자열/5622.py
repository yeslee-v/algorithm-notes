num = input(); result = 0

dial = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'],
        8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}

for i in num:
    for j, k in dial.items():
        # print(j, k) # 2 ['A', 'B', 'C'] .. 9 ['W', 'X', 'Y', 'Z']
        if i in k:
            result += (j+1)

print(result)