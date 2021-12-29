a = 12
b = 9
print(id(a))
def somthing():
    #global a              #for use global var as local
    a = 10                 #we can access gloabl var in func
    x = globals()['a']     #to acces all global var
    print(id(x))
    print("in func", a)    #local variable
    globals()['a'] = 14    #changing global var value

somthing()


print("outside", a)    #global variable