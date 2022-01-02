class Student:

    school = "KIIT"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):                            # instant method
        return(self.m1 + self.m2 + self.m3)/3       # its work with instant variable

    # def get_m1(self):  # get the value
       # return self.m1

    # def set_m1(self,value): # set the value
      # self.m1 = value
    @classmethod
    def getSchool(cls):                   # class methods
        return cls.school                          # works with class variable

    @staticmethod
    def info():                           # static methods
        print("Student are happy in the School..")     # extra with other things


s1 = Student(34, 56, 77)
s2 = Student(45, 56, 90)
print(s1.avg())
print(s2.avg())
print(s1.getSchool())
Student.info()