num=int(input("enter a number"))
if num==1:
    print("Not prime")
elif num == 0:
    print("Not prime")
else:
  for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
  else:
    print("prime")
