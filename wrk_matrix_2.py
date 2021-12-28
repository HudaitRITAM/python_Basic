from numpy import *
m = matrix('1 2 3;4 5 6;7 8 9')
m1 = matrix('0 1 7;6 2 8;7 5 4')
print(m)
print(diagonal(m))  #print diagonal element
print(m.min())   #minimum and maximum value
print(m.max())
m2 = m + m1  #addition of two matrix
print(m2)
m3 = m * m1  #multiplication of two matrix
print(m3)