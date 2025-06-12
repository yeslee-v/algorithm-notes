import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        Scanner scn = new Scanner(System.in);
        
        int i, a, sum = 0;
        for (i = 0; i < 5; i++) {
            a = scn.nextInt();
            list.add(a);
            
            sum += a;
        }
        
        System.out.println(sum / 5);
        
        Collections.sort(list);
        
        System.out.println(list.get(2));
    }
}