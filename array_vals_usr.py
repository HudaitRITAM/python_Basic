from array import *
arr = array('i',[])
n=int(input("Enter the length of the array :"))
for i in range(n):
    x=int(input("Enter the values : "))
    arr.append(x)

print(arr)
val=int(input("Enter the value for search :"))
k=0 #counter variable
for e in arr:
    if e==val:
        print(k,"is the index")
        break
    k += 1
else:
    print("not found")



