import java.util.Arrays;

/*
 * 문제 중: 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다
 * 신청 금액을 오름차순으로 정렬하고, 신청 금액이 가장 작은 것부터 예산에서 차감한다
 */
class Solution {
    public int solution(int[] d, int budget) {
        int i;

        Arrays.sort(d);
        for (i = 0; i < d.length; i++) {
            budget -= d[i];

            if (budget < 0) {
                return i; 
            }
        }

        return d.length;
    }
}