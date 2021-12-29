n = int(input('Enter length number: '))
if n < 0:
    print('invalid')
else:
    def fib(n):
        a = 0
        b = 1
        if n == 1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2, n):
                c = a + b
                a = b
                b = c
                print(c)
    fib(n)

#-------------alternative__________
#l=int(input("enter length: "))
#def fib(l):
#if l < 0:)
    #a = print("invalid input")
   # return a
    #a, b = 0, 1
    #for i in range(l):
       # print(a)
       # c = a + b
       # a = b
       # b = c
#fib(l)