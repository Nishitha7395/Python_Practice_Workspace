#SquaresCubesFunction.py
def squaresCubes():
	n=int(input("Enter How many Numbers you want to add in a List: "))
	if(n<=0):
		print("{} is invalid input".format(n))
	else:
		lst=list()
		for i in range(1,n+1):
			num=input("Enter {} NUmber: ".format(i))
			lst.append(num)
		print(lst)
		nsum,sqsum,csum=0,0,0
		print("-"*50)
		print("\tNumber:\tSquare\tCube")
		for i in range(0,len(lst)):
			print("\t{}\t{}\t{}".format(int(lst[i]),int(lst[i])**2,int(lst[i])**3))
			nsum=nsum+int(lst[i])
			sqsum=sqsum+int(lst[i])**2
			csum=csum+int(lst[i])**3
		print("-"*50)
		print("Sum:\t{}\t{}\t{}".format(nsum,sqsum,csum))
		print("-"*50)

#main program
squaresCubes()