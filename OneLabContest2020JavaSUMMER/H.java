import java.io.*; 
import java.util.Scanner;
  
public class H { 
    public static void main(String args[]) 
    { 

        Scanner in = new Scanner(System.in);
        String word = in.nextLine();
        String res = "";
        for(int i = 0; i < word.length(); i++) {
            if (Character.isLowerCase(word.charAt(i))) {
                res += Character.toUpperCase(word.charAt(i));
            } else {
                res += Character.toLowerCase(word.charAt(i));
            }
        }

        System.out.println(res);

    
    } 
}