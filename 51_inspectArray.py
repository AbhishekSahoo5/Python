import numpy as np

'''
Functions
----------
a.shape --- Array dimensions --> no. of columns,rows
len(a) -- length of array
b.ndim --- number of array dimensions
e.size -- Numb er of array elements
b.dtype -- Data type of array elements
b.astype(int)  -- convert on array to a different type

'''

a=[30,40,20,40,30]
arr=np.array(a)
print(arr)

print(arr.shape)
print(len(arr))
print(np.size(arr))
print(type(arr))
print(arr.dtype)
print(arr.astype(float))
print(arr.astype(str))

print("--------------------------------------")

b=[[10,20],[30,40]]
brr=np.array(b)
print(brr.shape)
print(len(brr))
print(np.size(brr))
print(brr.dtype)






