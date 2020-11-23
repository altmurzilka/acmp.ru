import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
  
class J { 
    public static void main(String args[]) 
    { 

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i<n; i++){
            int number = in.nextInt();
            if(!list.contains(number)) {
                list.add(number);
            }
        }
        Collections.sort(list);
        for(Integer i: list) {
            System.out.print(list.indexOf(i)+1);
            System.out.print(" ");
            System.out.print(i);
            System.out.println();
        }
    }
}