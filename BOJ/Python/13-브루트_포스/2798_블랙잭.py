n, m =  [int(e) for e in input().split(' ')]
arr = input()
arr_list = list(map(int, arr.split(' ')))

#idx arr_list의 인덱스
#ret 합계들 저장할 리스트 -> 후에 m과 비교할 값들
#arr_len 인풋 배열 길이
#cnt 선택된 횟수-> max 3
#total 더해진 값
def blackJack(idx, total, ret, arr_list, cnt):
    if idx >= len(arr_list): return
    if cnt == 3:
        if total <= m:
            ret.append(total)
        return
    blackJack(idx + 1, total + arr_list[idx], ret, arr_list, cnt + 1) # choosed
    blackJack(idx + 1, total, ret, arr_list, cnt)  # not choosed

ret = []
blackJack(0, 0, ret, arr_list, 0)
print(max(ret))