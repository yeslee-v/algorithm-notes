import java.util.ArrayList;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.InputStreamReader;
import java.util.Collections;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> list = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 1차 시간 초과
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());

        int input = 0;
        for (int i = 0; i < N; i++) {
            StringTokenizer sts = new StringTokenizer(br.readLine()); // 개행을 할 때마다 입력받을 token을 새로 만들어 줘야 함
            
            input = Integer.parseInt(sts.nextToken());
            
            list.add(input);
        }
        
        Collections.sort(list);
        
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        for (int i = 0; i < N; i++) {
            // 내부 버퍼에 입력값 모아둠
            bw.write(String.valueOf(list.get(i))); // 2차 시간 초과
            bw.newLine();
        }
        
        bw.flush(); // 출력 스트림에 있는 모든 데이터 한 번에 출력
        bw.close();
    }
}