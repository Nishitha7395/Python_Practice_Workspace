#SquaresCubesList.py
lst=[2,4,5,6,8,9,-10]
nsum,sqsum,csum=0,0,0
print("-"*50)
print("\tNumber:\tSquare\tCube")
for i in range(0,len(lst)):
	print("\t{}\t{}\t{}".format(lst[i],lst[i]**2,lst[i]**3))
	nsum=nsum+lst[i]
	sqsum=sqsum+lst[i]**2
	csum=csum+lst[i]**3
print("-"*50)
print("Sum:\t{}\t{}\t{}".format(nsum,sqsum,csum))
print("-"*50)