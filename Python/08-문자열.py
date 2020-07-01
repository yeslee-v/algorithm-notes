# # 11654_아스키 코드
#
# n = input()
# print(ord(n))
#
#
# # 11720_숫자의 합
#
# N = int(input()); num = int(input())
# answer = 0
#
# for i in str(num):
#     answer += int(i)
# print(answer)
#
#
# # 10809_알파벳 찾기
#
# S = input(); ls = []
#
# for i in S:
#     ls.append(i)
#
# for m in range(ord('a'), ord('z') + 1):
#     if chr(m) in ls:
#         print(ls.index(chr(m)))
#     else:
#         print(-1)
#
#
# # 2675_문자열 반복
#
# T = int(input())
# case = []
#
# for i in range(T):
#     R = input().split()
#     case.append(R)
#
# for m in range(T):
#     answer = []
#     for i in str(case[m][1]):
#         for j in range(1, int(case[m][0]) + 1):
#             result = i * j
#         answer.append(result)
#
#     print(''.join(answer))
#
#
# # 1157_단어 공부
#
# count_words = []
#
# words = input().upper()
# ls_words = list(set(words))
# # print(words, ls_words, count_words)    # MISSISSIPI ['I', 'S', 'M', 'P'] []
#
# for i in ls_words:
#     count = words.count(i)  # 4 4 1 1
#     count_words.append(count)
#
# if (count_words.count(max(count_words))) >= 2:
#     print("?")
# else:
#     print(ls_words[count_words.index(max(count_words))])
#
#
# # 1152_단어의 개수
#
# words = input().split()
# print(len(words))
#
#
# # 2908_상수
# # 1)
#
# ls_A = list(); ls_B = list()
# A, B = map(int, input().split())
#
# for i in str(A):
#     ls_A.append(i)
# ls_A.reverse()
# a = ''.join(ls_A)
#
# for j in str(B):
#     ls_B.append(j)
# ls_B.reverse()
# b = ''.join(ls_B)
#
# if a > b:
#     print(a)
# else:
#     print(b)
#
# # 2)
# print(max([''.join(reversed(i)) for i in input().split()]))
#
#
# # 5622_다이얼
#
# num = input(); result = 0
#
# dial = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
#         5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'],
#         8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}
#
# for i in num:
#     for j, k in dial.items():
#         # print(j, k) # 2 ['A', 'B', 'C'] .. 9 ['W', 'X', 'Y', 'Z']
#         if i in k:
#             result += (j+1)
#
# print(result)


# 2941_크로아티아 알파벳

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in alpha:
    a = a.replace(i, '@')
print(len(a))

