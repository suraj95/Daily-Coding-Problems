# Rotate a list by K elements

input=[1,2,3,4,5,6]
k=2    

# if k is bigger than length of input (multiple revolutions), then we will have to
# cut it down. For time being for simplicity, lets assume k is smaller than length of input

# output=[3,4,5,6,1,2]

output=[]

def rotate():
	for i in range(0,len(input)):
		if (i+k)<len(input):
			output.append(input[i+k])
		else:
			output.append(input[i+k-len(input)])

rotate()

print(output)

