/*
 * 선 비트 연산 후 2진법 변환! 
 * replace 함수를 여러개 사용할 수 있다
 */

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];

        int i;
        int combined = 0;
        String convertToString = "";
        for (i = 0; i < n; i++) {
            combined = arr1[i] | arr2[i];

            convertToString = Integer.toBinaryString(combined);

            answer[i] = convertToString.length() != n ? "0".repeat(n - convertToString.length()) + convertToString : convertToString;
        }

        for (i = 0; i < n; i++) {
            answer[i] = answer[i].replace('1', '#').replace('2', '#').replace('0', ' ');
        }

        return answer;
    }
}