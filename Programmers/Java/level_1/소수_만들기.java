import java.util.ArrayList;

/*
 * 3개 값 더하는 루프와 소수 판별 루프 분리
 * 소수 판별: 3개 더한 값의 제곱근까지 루프 돌려서 나머지가 0인지 확인 >> 전부 0이 아니면 소수
 * 0으로 나눠지는 경우, 플래그 변수 false로 바꾸고 break
 */
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        ArrayList<Integer> sumList = new ArrayList<Integer>();

        int i, j, k;
        for (i = 0; i < nums.length - 2; i++) {
            for (j = i + 1; j < nums.length - 1; j++) {
                for (k = j + 1; k < nums.length; k++) {
                    sumList.add(nums[i] + nums[j] + nums[k]);
                }
            }
        }

        int sqrt = 0;
        boolean isPrime = true;
        for (Integer sum: sumList) {
            sqrt = (int)Math.sqrt((double)sum);

            isPrime = true;
            for (i = 2; i <= sqrt; i++) {
                if (sum % i == 0) {
                    isPrime = false;

                    break;
                }
            }

            if (isPrime) {
                answer++;
            }
        }

        return answer;
    }
}