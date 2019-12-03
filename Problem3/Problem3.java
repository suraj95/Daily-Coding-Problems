//Sort a given array of 0s and 1s
// You cannot count or add the elements of the array
// You cannot use another array
import java.util.*;

public class Problem3{
    
     public static int[] sort_my_arr(int[] arr)
    {
        int left = 0;
        int right = (arr.length)-1;

        while(left<right)
        {
            while((arr[left]==0) && (left<right))
            {
                left+=1;
            }

            while((arr[right]==1) && (left<right))
            {
                right-=1;
            }

            if(left<right){
                arr[left]=0;
                arr[right]=1;
                left+=1;
                right-=1;
            }
        
        }
        
        return arr;
    }
    
    
    public static void main(String[] args)
    {
       int[] my_arr = new int[]{1,1,1,0,0,0};
        Problem3 obj = new Problem3();
        int[] res = obj.sort_my_arr(my_arr);
        for(int i=0;i<res.length;i++){
        System.out.print(res[i]+" ");
        }
        
    }

   
}
