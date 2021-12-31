class computer():
    def __init__(self):
        self.name = "Ritam"
        self.age = "21"

    def update(self):
        self.age = "25"

    def compare(self, other):       # compare(who is calling,whom to compare)
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()        # constructor
c1.age = 30
c2 = computer()        # constructor

if c1.compare(c2):          # c1 becomes self and c2 becomes other
    print("they are same")
else:
    print("they are different")

# c1.update()           # self referring to object ,here c1 referred

# print(id(c1))          # print the memory location of c1 object
# print(id(c2))

print(c1.age)
print(c2.age)

