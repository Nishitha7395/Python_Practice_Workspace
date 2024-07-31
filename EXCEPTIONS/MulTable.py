# MulTable.py
from invalid import InvalidInputError,ZeroError

def table():
	n=int(input("Enter a Number: ")) # implictly PVM raises value error
	if(n<0):
		raise InvalidInputError
	elif(n==0):
		raise ZeroError
	else:
		print("-"*40)
		print("Multiplication table for {}".format(n))
		print("-"*40)
		for i in range(1,11):
			print("{}X{}={}".format(n,i,n*i))
		print("-"*40)