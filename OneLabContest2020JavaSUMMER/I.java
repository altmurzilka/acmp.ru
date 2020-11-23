import java.io.*; 
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
  
public class I { 
    public static void main(String args[]) 
    { 

        Scanner in = new Scanner(System.in);
        String word = in.nextLine();
        ArrayList<Character> res = new ArrayList<Character>();
        for(int i = 0; i < word.length(); i++) {
            if (!res.contains(word.charAt(i))) {
                res.add(word.charAt(i));
            } 
        }

        String answer = "";
        Collections.sort(res);
        for(Character c: res){
            answer = answer+ c; 
        }
        System.out.println(answer);
        System.out.println(factorial(answer.length()));

    
    } 

    public static long factorial(int number) {
        long result = 1;

        for (int factor = 2; factor <= number; factor++) {
            result *= factor;
        }

        return result;
    }
}