import java.util.stream.IntStream;

/*
 * 처음에는 일일이 찾아서 더하는걸 생각했다가
 * 아래처럼 0부터 9까지의 합에서 numbers의 합을 빼거나
 * 전체에서 numbers[i]를 빼는 방법을 배웠다
 */
class Solution {
    public int solution(int[] numbers) {
        int sumOfAllNumebr = 45;
        int sumOfNumbers = IntStream.of(numbers).sum();

        return sumOfAllNumebr - sumOfNumbers;
    }
}