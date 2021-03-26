import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
	
	private static final Scanner scanner = new Scanner(System.in);
	
	public static void main(String[] args){
		BigIntegern n = scanner.nextBigInteger();
		scanner.close();
		
		if(n.isProbablePrime(50)) {
			System.out.println("prime");
		}
		else
		{
			System.out.println("not prime");
		}
	}
}
	