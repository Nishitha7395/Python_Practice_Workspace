#FactorialOOP.py
class Factorial:
	def __init__(self):
		self.n=int(input("Enter a Number you want to calculate its Factorial !: "))

	def calFactorial(self):
		if(self.n<=0):
			print("Invalid Input")
		else:
			fact=1
			for i in range(1,self.n+1):
				fact=fact*i
				
			print("Factorial of {}! = {}".format(self.n,fact))
			print("Factors of {} :".format(self.n))
			for i in range(1,self.n+1):
				if(self.n%i==0):
					print("{}".format(i),end=" ")


#main program
obj=Factorial()
obj.calFactorial()

