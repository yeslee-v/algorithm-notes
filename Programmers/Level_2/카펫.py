import math

def solution(brown, yellow):
    w, h, answer = []
    
    total = brown + yellow

    for i in range(1, int(math.sqrt(total)) + 1):
        if total % i == 0:
            h.append(i)

    for i in h:
        w.append(int(total / i))

    for i in range(len(w)):
        if (w[i] - 2) * (h[i] - 2) == yellow:
            answer.append[w[i]]
            answer.append[h[i]]
            break

    return answer

answer1 = solution(10, 2)
answer2 = solution(8, 1)
answer3 = solution(24, 24)

print(answer1)
print(answer2)
print(answer3)