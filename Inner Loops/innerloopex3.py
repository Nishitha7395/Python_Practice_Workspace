#innerloopex3.py
i=1
while i<5:
	print("-"*50)
	print("Value of i={}".format(i))
	print("-"*50)
	for j in range(1,4):
		print("\tValue of j={}".format(j))
	else:
		print("-"*50)
		print("Out of Inner for loop")
	i=i+1
else:
	print("-"*50)
	print("Out of Outer While loop")
	print("-"*50)
