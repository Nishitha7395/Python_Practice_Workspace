#multables.py
n=int(input("Enter the number of Inputs you want to add in List: "))
if(n<=0):
	print("Invalid Input")
else:
	lst=list()
	for i in range(1,n+1):
		val=int(input("Enter the {} value: ".format(i)))
		lst.append(val)
	else:
		print(lst)
		print("-"*30)
		for n in lst:
			if(n<=0):
				print("{} is invalid input".format(n))
			else:
				print("-"*30)
				print("Multiplication table for {}".format(n))
				print("-"*30)
				for i in range(1,11):
					print("{} X {} = {}".format(n,i,n*i))
				else:
					print("-"*30)
	
	