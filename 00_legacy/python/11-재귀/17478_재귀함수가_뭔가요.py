n = int(input())

def recur_func(cnt, n):
    if cnt > n: return
    re_str1 = """"재귀함수가 뭔가요?\""""
    re_str2 = """"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."""
    re_str3 = """마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."""
    re_str4 = """그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""""
    print('____' * cnt + re_str1)
    if cnt == n:
        print('____' * cnt + """"재귀함수는 자기 자신을 호출하는 함수라네\"""")
    else:
        print('____' * cnt + re_str2)
        print('____' * cnt + re_str3)
        print('____' * cnt + re_str4)

    recur_func(cnt + 1,n)
    re_str = """라고 답변하였지."""
    print('____' * cnt + re_str)
    
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recur_func(0, n)