class Solution {
  public int solution(int n) {
    int answer = 0;
    
    // n이 0, 1일 때 핸들링
    if (n == 0) {
        return answer;
    } else if (n == 1) {
        return 1;
    } else if (n == -1) {
        return -1;
    }
    
    int i;
    double a;
    
    if (n > 0) { // n이 양수
        answer = 1 + n;
        a = Math.sqrt(n);
        
        for (i = 2; i <= (int)a; i++) {
          if (n % i == 0) {
              answer += (i == (n / i)) ? i : i + (n / i);
            } 
        }
    } else { // n이 음수
        answer = -1 + n;
        a = Math.sqrt(-1 * n);
    
        for (i = -2; i >= (-1 * (int)a); i--) {
            if (n % i == 0) {
              answer += (i == (-1 * (n / i))) ? i : i + (-1 * (n / i));
            } 
        }
    }
    
    return answer;
  }
}