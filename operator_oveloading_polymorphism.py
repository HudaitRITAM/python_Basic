class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):            # operator overloading
        p = self.m1 + other.m1
        q = self.m2 + other.m2
        r = Student(p, q)
        return r

    def __gt__(self, other):              # operator overloading
        a = self.m1 + self.m2
        b = other.m1 + other.m2
        if a > b:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(56, 87)
s2 = Student(30, 70)
s3 = s1 + s2                 # by default its make sense that Student.__add__(s1+s2)
if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")

print(s3.m1)
print(s1)
print(s2)