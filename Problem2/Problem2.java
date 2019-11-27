/*
 	Problem Statement :- Given a number 'n' find the floor of sqrt of n
 	Time Complexity - O(sqrt(n))
*/
import java.util.*;
class Problem2 {
	public static int sqrt(int n) {
		if (n <= 1) return n; // for n -> less than equal to 1 we can return that number itself
		// picking start and end as the range for binary search
		int start = 0;
		int end = n;
		int ans = 1;
		while (start < end) {
			int mid = (start+end)/2;
			if (mid*mid == n) {
				// now if the number is perfect square we can reach this statement.
				ans = mid;
				return ans; // just found the ans and return it
			}
			if (mid*mid < n) {
				// since we need to find floor, so we can consider this case for number which are not perfect square..
				ans = mid;
				start = mid+1; // make the search space reduce towards the left side... 
			}else {
				// here we don't need to make ans == mid as we are finding floor
				// but for finding roof .. make sure to equate ans = mid under this statement
				// go search towards the right half.. as mid*mid > n..
				end = mid;
			}
		}
		return ans;
	}
	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		int ans = sqrt(n);
		System.out.println(ans);
	}
}
