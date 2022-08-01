count_words = []

words = input().upper()
ls_words = list(set(words))
# print(words, ls_words, count_words)    # MISSISSIPI ['I', 'S', 'M', 'P'] []

for i in ls_words:
    count = words.count(i)  # 4 4 1 1
    count_words.append(count)

if (count_words.count(max(count_words))) >= 2:
    print("?")
else:
    print(ls_words[count_words.index(max(count_words))])