Input= [0,1,-2,3,4,0,5,-27,9,0]
Output = [1,-2,3,4,5,-27,9,0,0,0]

sample_array = [0,0,-3,4,0,0,9]
zero_count=0
result=[]

for item in sample_array:
	if item==0:
		zero_count+=1
	else:
		result.append(item)

for i in range(zero_count):
	result.append(0)	

print(result)
