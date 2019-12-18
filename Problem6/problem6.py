

input = [3,6,4,6,1,3,4,1,7]
output = [3,6,4,1,7] # removed duplicates 6,4,1,3

# O(n) time and O(1) space

# detect duplicates in 1 iteration and allocate the same number of pointers irrespective of the list size

num_list = []
num_integers = 10   # assuming the numbers are in range 0-9
for i in range(num_integers):
	num_list.append(i)

# dictionary of all numbers initialized with count 0
num_dict= {key: 0 for key in num_list}

result = []

for item in input:
	if num_dict[item]==0:  # This is not a duplicate. So add to result. 
		result.append(item)
	else:		       # This is a duplicate. Don't add to result
		pass

	num_dict[item]+=1

print(result)

	
