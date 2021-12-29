def person(name, **kw):  # ** means passing multiple arg,but with the help of keywords
    print(name)
    for i,j in kw.items(): #i,j for key and value
        print(i,j)

person('ritam', age=21, city='medinipur', mob=9876543210)