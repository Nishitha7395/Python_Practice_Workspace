#reduceex1.py
import functools
print("Enter list of elements seperated by space:")
lst=[int(val) for val in input().split()]
res=functools.reduce(lambda x,y:x+y,lst)
print("Type of res=",type(res))
print("Sum=",res)