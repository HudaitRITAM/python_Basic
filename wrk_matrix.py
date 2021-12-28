from numpy import *
arr1 = array([
               [2, 5, 6, 4],
               [1, 2, 3, 14]
             ])
arr2 = arr1.flatten() #flat the array or make it two dimenssion to one dimenssion
arr3 = arr2.reshape(4, 2) #to make 1d to other dimention array
arr4 = arr2.reshape(2, 2, 2)  #3d array contains 2d array in it
m = matrix(arr1)   #making matrix from array
print(arr4)
print(arr3)
print(arr2)
print(arr1)
print(m)
print(arr1.dtype)  #data type of the array
print(arr1.ndim) #dimension of the array(rankking)
print(arr1.shape)  #no. of rows and colmn
print(arr1.size)   #size of entire block