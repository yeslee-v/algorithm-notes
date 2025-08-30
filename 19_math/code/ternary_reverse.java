/*
 * Math.pow(): 부동소수점 연산 사용해서 정밀도 떨어짐 -> 직접 연산하는 것이 좋다
 * data type을 신경쓰자(max int)
 */

class Solution {
  public int solution(int n) {
      long tmp = 0, pow = 1;
      int cnt = 0;

      int quot = n;

      while (0 < quot) {
          tmp += (long) (quot % 3) * pow;

          quot /= 3;
          pow *= 10;
          cnt++;
      }

      int answer = 0;
      while (0 < cnt) {
          cnt--;

          answer += (tmp % 10) * Math.pow(3, cnt);

          tmp /= 10;
      }

      return answer;
  }
}