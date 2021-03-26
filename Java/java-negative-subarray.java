import java.util.*;
import java.io.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] arr = new int[n];
        
        for(int i=0;i<n;i++){
        arr[i]=scan.nextInt();
    }
        int negNum = 0;
        for(int j=0;j<n;j++)
        {
            int sum=0;
            for(int k=j;k<n;k++){
                sum = arr[k]+sum;
                
                if(sum < 0) {
                    negNum++;
                }
            }
        }
        System.out.println(negNum);
    }
}