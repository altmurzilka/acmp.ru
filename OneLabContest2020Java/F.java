import java.io.*; 
import java.util.Scanner;
import java.util.HashMap;
  
public class F { 
    public static void main(String args[]) 
    { 
        HashMap<String,String> dict = new HashMap<String,String>();
        Scanner in = new Scanner(System.in);
        String[] lines = new String[in.nextInt()];
        in.nextLine();
        for (int i = 0; i < lines.length; i++){
            lines[i] = in.nextLine();
            
        }
        for(String line: lines) {
            String[] l = line.split(" ");
            for(int j = 0; j < Integer.parseInt(l[1]); j++){
                dict.put(l[j+2],l[0]);
            }
        } 
        
        
        Scanner userIn = new Scanner(System.in);
        int m = userIn.nextInt();
        String[] cities = new String[m];
        userIn.nextLine();
        for (int i = 0; i < m; i++){
            cities[i] = userIn.nextLine();
        }
        for (int i = 0; i < m; i++){
            if(dict.containsKey(cities[i])){
                System.out.println(dict.get(cities[i]));
            } else {
                System.out.println("Unknown");
            }
            
        }


    
    } 
} 