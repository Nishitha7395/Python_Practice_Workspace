#kwdparamex1.py
def disp(a,b,c,d=40): # here d is default args
	print("{}\t{}\t{}\t{}".format(a,b,c,d))

#main program
print("-"*50)
print("a\tb\tc")
print("-"*50)
disp(10,20,30) # Function call--Possitional args
disp(c=30,a=10,b=20) # function call--Keyword  args
disp(10,c=30,b=20) # function call -- Possitional and KWD args
disp(10,20,d=45,c=30) # function call -- Positional, KWD and Default args

print("-"*50)