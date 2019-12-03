# created by adanai at 2019-12-02 13:05.
# 
# Given an array of integers, return a new array such that,
# each element at index i of the new array is the product of 
# all the numbers in the original array except the one at i

arr = [3, 2, 1] #defining a random array
def arr_prod(l): #defining the function
    fin_arr = [] #initializing an empty result array
    count_index = 0 #using a count_index to compare with the input array index
    
    #The idea is to iterate over input array and check if index is equal to index_count
    #which is reference to whether the element should be multiplied or not
    for i in range(0, len(l)): 
        prod = 1 #intializing value of element in result array
        for ele in l:
            
            #if the count_index and array index don't match, multiply to variable prod
            if count_index != l.index(ele): 
                prod *= ele
        fin_arr.append(prod) #update the result array
        count_index += 1 #update reference index
    
    return(fin_arr)


print(arr_prod(arr))
