from functools import *

nums = [5, 6, 46, 78, 0, 40, 87, 35, 7, 680, 79]

even = list(filter(lambda n: n % 2 == 0, nums))    # use of filter func for filter needed value from large value
                                                   # lambda func use inside it for running the function
print(even)
doubles = list(map(lambda n: n * 2, even))         # use map to make a operation with the filtered value
print(doubles)

sum = reduce(lambda a, b: a+b, doubles)          # use a perticular operation with all values and give one value
print(sum)