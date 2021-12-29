def person(name, age):
    print(name)
    print(age)


person('Ritam', 21) #positon agruments
person(age=21, name='Ritam') #keywords arguments

def person1(name1, age1=18):  #default arguments
    print(name1)
    print(age1)


person1('Rit')

def sum(* b):    # *b updated the value of b and make it tupple
    c = 0
    for i in b:   # make the function for update the value in c after sum of b each time
        c = c + i
    print(c)


sum(3, 4, 24, 78)  #variable length arguments