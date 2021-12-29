# function is a blcok where will have one task
def add_sub_mul(x, y):    #define your own function.
    a = x + y
    b = x - y
    c = x * y
    return a, b, c      #return the value of each operation

result1,result2,result3 = add_sub_mul(4, 5)     #call the function

print(result1, result2, result3)
