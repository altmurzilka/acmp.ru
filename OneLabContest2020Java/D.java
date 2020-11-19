import java.io.*; 
import java.util.Scanner;
  
public class D { 
    public static void main(String args[]) 
    { 
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for(int i = 0; i < n; i++) {
            int j = 0;
            for(int k = 0; k < i; k++) {
                System.out.print(i-j+1);
                System.out.print(" ");
                j += 1;
            }
            j = 0;
            for(int l = i; l < n; l++) {
                System.out.print(j+1);
                System.out.print(" ");
                j += 1;
            }
            System.out.println();

        }    
    } 
} 