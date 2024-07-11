import numpy as np

arr=np.array([10,20,30,40])     #1-d array
print(arr)

# arr=np.array([[10,20,30,40],[50,60,70,80]])    #2-d array
# print(arr)

print(type (arr))

#slicing
print(arr[0:3])
print(arr[3:])
print(arr[2:])

print("---------------------------------------------")

arr=np.array([[10,20,30,40],[50,60,70,80]])
print(arr[0:2,0:3])
print(arr[0,1:3])
print(arr[1,1:3])

# shape of the matrix
print(np.shape(arr))

#size of matrix
print(np.size(arr))

#print the dimensions
print(np.ndim(arr))

# print the datatype used
print(arr.dtype)