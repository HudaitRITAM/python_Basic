def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


x = int(input("what number factorial do you want :\n"))

result = fact(x)
print(result)