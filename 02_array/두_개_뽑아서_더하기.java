import java.util.Arrays;
import java.util.ArrayList;

/*
 * answer의 크기 알 수 없음 -> 동적으로 크기가 변하는 Integer형 ArrayList 선언
 * Stream API 사용하여 int형 배열로 변환
 * ArrayList 대신 set(HashSet, TreeSet) -> 중복 제거
 * TreeSet 사용하면 자동 정렬
 */

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};
        ArrayList<Integer> answerList = new ArrayList<>();

        Arrays.sort(numbers);

        int sum = 0;
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                sum = numbers[i] + numbers[j];

                if (!answerList.contains(sum)) {
                    answerList.add(sum);
                }
            }
        }

        answer = answerList.stream().mapToInt(i -> i).toArray();

        Arrays.sort(answer);

        return answer;
    }
}