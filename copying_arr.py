from numpy import *
arr1 = array([1, 2, 3, 4, 5])
arr4 = array([123, 34, 567, 90])
# arr5 = arr1 (copy the value and adress both)
#arr5 = arr1.view() (adress are different but they depent on each other.).means shalow copy
arr5 = arr1.copy()  #here they not depend each other...deep copy
arr1[1] = 6  #after cahnge the arr1 value arr5 remain uncahnged
print(arr1)
print(arr5)
print(id(arr1))
print(id(arr5))
#............................
arr2 = arr1 + 5
print(arr2)
#...............................
arr3 = arr1 + arr2
print(arr3)
#...............................
print(sqrt(arr1)) #sqrt root of array element
#...............................
print(sum(arr2)) #sum of all element in array2
#...............................
print(min(arr1)) #minimum value of arr1
#................................
print(max(arr4)) #maximum value of arr4
#...............................
print(sort(arr4)) #sorted the arr4 in accending order
#..............................
print(concatenate([arr1, arr4])) #concatenate two array
#..............................
