# created by adanai at 2019-11-27 23:33.

# Find the square root of a number without using in-built library functions. 
# If the number is not a perfect square, use the floor of the square root.

def sr(n):
    if n <= 1:
        return n #return the number as its square root if it is less than 1

   #initialize the start/stop parameters for the 'binary search' 
    start = 0
    end = n
    ans = 1 # ans is the variable that will be returned

    while(start < end):
        mid = (start+end)//2 #divide and conquer, divide the number by 2 and eliminate ranges
        if mid*mid == n: #checking the most basic condition in the spirit of binary search
            ans = mid 
            break
        if mid*mid < n:
            ans = mid
            start = mid+1 #shrinking the search space from the left towards 'n'
        else:
            end = mid #shrinking the search space from the right away from 'n'
    return ans  

res = sr(37)
print(res) #prints 6

