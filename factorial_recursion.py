def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)     # as for 5! it return 5*(calling fact func for 4!)


x = int(input("A number for factorial :"))
result = fact(x)
print(result)