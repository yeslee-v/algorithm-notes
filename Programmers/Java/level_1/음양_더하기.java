public int solution(int[] absolutes, boolean[] signs) {
    int answer = 123456789;

    int i, j;
    int real = 0;
    int result = 0;

    for (i = 0; i < absolutes.length; i++) {
        j = signs[i] ? 1 : -1;
        real = absolutes[i] * j;
        result += real;
    }

    return result;
}