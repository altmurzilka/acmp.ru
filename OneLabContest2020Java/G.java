import java.io.*; 
import java.util.Scanner;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
  
public class G { 
    public static void main(String args[]) 
    { 
        HashMap<String,Integer> dict = new HashMap<String,Integer>();
        Scanner in = new Scanner(System.in);
        String[] names  = in.nextLine().split(" ");
        for(String name: names) {
            if(dict.containsKey(name)){
                int val = dict.get(name).intValue();
                val++;
                dict.put(name, val);
            } else {
                dict.put(name,1);
            }
        }
        ArrayList<String> res = new ArrayList<>();
        for (HashMap.Entry mapElement : dict.entrySet()) { 
             
            int value = ((int)mapElement.getValue()); 
            if (value % 2 == 0) {
                String key = (String)mapElement.getKey();
                res.add(key);
            }
  
        }

        Collections.sort(res);
        for(String name: res) {
            System.out.println(name);
        }

        
    } 
} 