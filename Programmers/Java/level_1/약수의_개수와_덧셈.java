package level_1;
class Solution {
    public int solution(int left, int right) {
        int answer = 0, result = 0;

        for (int i = left; i <= right; i++) {
            int sqrt = (int)Math.sqrt((double)i);

            for (int j = 1; j <= sqrt; j++) {
                if (i % j == 0) {
                    result += j == i / j ? 1 : 2;
                }
            }

            answer += result % 2 == 0 ? i : -1 * i;

            result = 0;
        }

        return answer;
    }
}