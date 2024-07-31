#Program for searching exactly one 'k' or more 'k'
#RegExp24.py
import re
mattab=re.finditer("k+","kvkkvkkkvkv")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp24.py
--------------------------------------------------
Start Index: 0 End Index: 1 Value: k
Start Index: 2 End Index: 4 Value: kk
Start Index: 5 End Index: 8 Value: kkk
Start Index: 9 End Index: 10 Value: k
--------------------------------------------------
'''