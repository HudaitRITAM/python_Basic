# to get square up to 10
def topten():
    n = 1
    while n <= 10:
       sq = n*n
       yield sq         # return value as the format of iterator
       n += 1                 # return will terminate the function it will not


values = topten()
for i in values:
 print(i)
