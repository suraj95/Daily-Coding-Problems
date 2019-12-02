# created by adanai at 2019-12-02 10:59.
# 
# Given an array of integers, return a new array such that,
# each element at index i of the new array is the product of 
# all the numbers in the original array except the one at i

arr = [1, 2, 3, 4, 5] #defining a random array

def arr_prod(l): #function definition for the problem
    prod = 1 #initializing a product variable
    for i in l:
        prod = prod*i #obtaining the product of the array
    #creating an array of the size of given array 
    # with identical elements equal to the product
    fin_arr = [prod]*len(l) 
    #dividing the product in fin_arr by element of arr
    fin_arr = [fin_arr[i]//l[i] for i in range(0, len(l))]
    return fin_arr
    
print(arr_prod(arr))
