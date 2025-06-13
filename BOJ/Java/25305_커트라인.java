import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        Scanner scn = new Scanner(System.in);
        
        int N = scn.nextInt();
        int k = scn.nextInt();
        
        int input;
        for (int i = 0; i < N; i++) {
            input = scn.nextInt();
            
            list.add(input);
        }
        
        Collections.sort(list, Collections.reverseOrder());
        
        System.out.println(list.get(k - 1));
    }
}