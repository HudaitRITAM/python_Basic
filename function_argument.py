def update(x):
  print(id(x))          #call a function to pass by value they will share the same id
                        # when you change the value it wil change the address

  x = 8
  print(id(x))
  print('x', x)

a = 10
print(id(a))
update(a)
print('a', a)

