class Student:              # outer class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.age)
        self.lap.show()

    class Laptop:          # inner class
        def __init__(self):
            self.brand = 'HP'
            self.ram = 8
            self.cpu = 'i7'

        def show(self):
            print(self.brand, self.ram, self.cpu)


s1 = Student('Ritam', 21)
s2 = Student('Sneha', 20)

s1.show()
s2.show()
# lap1 = Student.laptop
# lap2 = Student.laptop

# lap1 = s1.lap
# lap2 = s2.lap
# print(id(lap1))
# print(id(lap2))