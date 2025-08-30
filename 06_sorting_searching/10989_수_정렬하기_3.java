import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.lang.StringBuilder;
import java.util.Arrays;

/*
 * 시간 줄이기
 * 1. BufferedReader 사용: Scanner보다 빠름
 * 2. 하나씩 입력받을 때: StringTokenizer가 필요하지 않음 >> 바로 readLine()으로 입력받음
 * 3. ArrayList 대신 배열 사용
 * 4. Counting Sort: O(N + K) 시간 복잡도
 * 5. StringBuilder로 출력: write를 N번 순회하는 BufferedWriter 대신 한 번에 출력
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] inputArr = new int[N];

        int input = 0;
        for (int i = 0; i < N; i++) {
            input = Integer.parseInt(br.readLine());
            
            inputArr[i] = input;
        }
        
        int[] result = countingSort(inputArr, N);
        
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < N; i++) {
            if (i == N - 1) {
                sb.append(result[i]);
            } else {
                sb.append(result[i]).append("\n");
            }
        }
        
        System.out.println(sb);
    }
    
    static int[] countingSort(int[] inputArr, int N) {
        // 1. get inputArr max value
        int max = inputArr[0];

        for (int num: inputArr) {
            max = Math.max(max, num);
        }
        
        // 2. create array as max + 1 size for counting
        int[] countArr = new int[max + 1];
        
        // 3. calculate how may inputArr element per index and save at countArr
        for (int input: inputArr) {
            countArr[input]++;
        }
        
        // 4. calculate cumulative frequency of positioning 
        int i;
        for(i = 0; i <= max; i++) {
            countArr[i] = i == 0 ? countArr[i] : countArr[i - 1] + countArr[i];
        }
        
        // 5. create array as N size for save sorted result
        int[] outputArr = new int[N];
        
        // 6. reverse traversal for stable sorting
        for (i = N -1; i >= 0; i--) {
            outputArr[countArr[inputArr[i]] - 1] = inputArr[i];
            countArr[inputArr[i]]--;
        }
        
        return outputArr;
    }
}