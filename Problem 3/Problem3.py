# created by adanai at 2019-11-28 18:44.
# 
# Sort a given array of 0s and 1s
# You cannot count or add the elements of the array
# You cannot use another array

def sort_arr(arr):
    #define the reference indices
    left = 0
    right = len(arr)-1

    while left < right: #to avoid overlapping of operations
        while arr[left] == 0 and left < right: #skip the already sorted 0s
            left += 1 #iterate
        
        while arr[right] == 1 and left < right: #skip the already sorted 1s
            right -= 1 #iterate
        
        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1
    return arr

print(sortArr([0, 0, 1, 1, 0, 1])) #returns [0, 0, 0, 1, 1, 1]
