public long solution(int price, int money, int count) {
    long answer = 0;

    int i;
    for (i = 1; i <= count; i++) {
        answer += (price * i);
    }

    return answer - money > 0 ? answer - money : 0;
}