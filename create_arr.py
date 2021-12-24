from numpy import *
arr1 = array([1, 2, 3, 4, 5])  #if want float or intdatatype you can write after putting the value
print(arr1)
arr2 = linspace(0,15,5)  #by default its create 50,if don't give 5
print(arr2)
arr3 = logspace(1, 40, 5)  #1 to 40 basically make 5 part with log base 10
print(arr3)
arr4 = arange(1, 15, 2)  #create array 1 to 15 with 2 gap
print(arr4)
arr5 = ones(2, int)  #by default its make float vaule,if write int its show int value
print(arr5)
arr6 = zeros(5,int) #by default it also showing float
print(arr6)