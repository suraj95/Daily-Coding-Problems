# created by adanai at 2019-11-25 16:18.
# 
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def summa(l,k):  #definition of function
    s = set()   #creation of empty set (hash-set in java)
    for ele in l:   #iterating through the list
        diff = k - ele   #taking the remainder
        if diff in s:   #checking if difference is there in the set
            return True   #break out of the loop if the difference already exists in the set
        s.add(ele)   #add the element of the list to the set, which would be a reference to match with future "differences"
    return False   #In case no differences match with the elements in the set, it means no two numbers add to 'k', thus returning false

print(summa([10,15,3,7],17))
