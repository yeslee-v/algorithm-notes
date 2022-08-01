def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == s1[i % 5]:
            correct[0] += 1
        if answers[i] == s2[i % 8]:
            correct[1] += 1
        if answers[i] == s3[i % 10]:
            correct[2] += 1

    for idx, value in enumerate(correct):
        if value == max(correct):
            answer.append(idx + 1)

    return answer

a1 = solution([1, 2, 3, 4, 5])
a2 = solution([1, 3, 2, 4, 2])

print(a1, a2)