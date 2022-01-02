# how constructor behave in inheritance
# how to use super() in inheritance
# Method Resolution Order

class A:
    def __init__(self):
        print("init A ")

    def feature1(self):
        print("feature 1_A is working")

    def feature2(self):
        print("feature 2 is working")


class B:
    def __init__(self):
        # super().__init__()   # to use the constructor of super class A
        print("init B ")

    def feature1(self):
        print("feature 1_B is working")

    def feature4(self):
        print("feature 4 is working")


class C(A, B):
    def __init__(self):
        super().__init__()     # prefer left one first ,then right
        print("init C ")

    def feat(self):
        super().feature2()


a1 = C()
# a1.feature1()                        # MRO ...always left one first prefer
a1.feat()              # to present super class we use super method
