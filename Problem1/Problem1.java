/*
Tag :- EASY | Google
Problem 1: Given a list of numbers and a number k, return whether any two 
		 numbers from the list add up to k.

for ex :- given [10, 15, 3, 7] and k is 17,
return true since 10+7 is 17.

Bonus :- Do it in O(N)
*/
import java.util.*;
class Problem1 {
	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		int []arr = {50 ,10, 15, 3, 7};
		// {50, 10, 15, 3, 7} -> set
		int k = 17;
		HashSet<Integer> set = new HashSet<>();
		for (int i = 0; i < arr.length; i++) {
			int t = k - arr[i]; 
			if (set.contains(t)) {
				// it contains a pair which adds up to the sum
				System.out.println("The array contains the sum " + k + " and the elements that adds up to it are " + arr[i] + " and "+t);
			}
			// add it to set..
			set.add(arr[i]);
		}
	}
}
