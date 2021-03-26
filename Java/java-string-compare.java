import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        for(int i=0;i<(s.length() - k +1);i++)
        {
            String subS = s.substring(i,i+k);
            if(subS.compareTo(smallest)<0 | i==0)
                smallest = subS;
            if(subS.compareTo(largest)>0 | i==0)
                largest = subS;
        }
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
		
        System.out.println(getSmallestAndLargest(s, k));
    }
}


/*
public static void main(String[] args) {
    * Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. *
    Scanner scan=new Scanner(System.in);
    String str=scan.next();
    int k=scan.nextInt();
    SortedSet<String> sets=new TreeSet<String>();
    for(int i=0;i<=str.length()-k;i++){
        sets.add(str.substring(i,i+k));
    }
    System.out.println(sets.first());
    System.out.println(sets.last());
}
*/