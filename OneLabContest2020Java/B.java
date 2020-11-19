import java.io.*; 
import java.util.Scanner;
  
public class B { 
    public static void main(String args[]) 
    { 

        Scanner in = new Scanner(System.in);
        String sentence = in.nextLine();
        String[] arrayOfWords = sentence.split(" ");
        for(String word: arrayOfWords){
            System.out.print(word.length());
            System.out.print(" ");
        }
        System.out.println();

    
    } 
} 