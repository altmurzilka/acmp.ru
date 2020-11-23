import java.io.*; 
import java.util.Scanner;
  
class A { 
    public static void main(String args[]) 
    { 

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int arr[] = new int[n+1];
        for(int i = 1; i<n; i++){
            arr[i] = in.nextInt();
        }
        int even = 0, num = 0; 
  
        for (int i = 1; i < arr.length; i++) { 
            if (i % 2 != 0){
                if(arr[i] % 2 == 0) {
                    even += arr[i];
                    num++;
                }
            }
             
                 
        } 
        double res = (double) even/num;
        if(res % 1 == 0) {
            int value = (int)res;
            System.out.println(value);
        } else {
            res = Double.parseDouble(String.format("%.6f", res));
            System.out.println(res);
        }
    
    } 
} 