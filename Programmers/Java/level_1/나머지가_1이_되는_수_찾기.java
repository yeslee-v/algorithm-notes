package level_1;
class Solution {
  public int solution(int n) {
      int x = 0;
      
      // n이 3의 배수는 무조건 2을 반환한다 >> 추가해도 시간 복잡도는 O(n)으로 동일
      //if (n % 3 == 0 && n % 2 != 0) {
      //    return 2;
      //}
      
      // 시간복잡도를 고려한다면 다음과 같이 작성하는 것이 좋다
      if (n % 2 == 1) return n;

      int a = n - 1; // 나머지가 1이어야 하므로 1을 뺀 값에서 1을 제외한 가장 작은 약수를 구한다.
      
      // 반례: n = 7 -> 7 % 2 = 1
      //if (a % 3 == 0) {
        //  return 3;
      //}
      
      double b = Math.sqrt(a);
      boolean isResult = false;
      
      for (int i = 2; i <= (int)b; i++) {
          if (a % i == 0) {
              isResult = true;
              
              return i;
          }
      }
      
      if (isResult == false) {
          return a;
      }
      
      return x;
  }
}