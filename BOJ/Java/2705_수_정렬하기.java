import java.util.ArrayList;
import java.util.Collections; // Collections 패키지
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        Scanner scn = new Scanner(System.in);
        
        int N = scn.nextInt();
        
        int a, i;
        for (i = 0; i < N; i++) {
            a = scn.nextInt();
            
            arr.add(a);
        }
        
        Collections.sort(arr); // 기본: 오름차순 정렬
        
        for (i = 0; i < N; i++) {
            System.out.println(arr.get(i));
        }
    }
}