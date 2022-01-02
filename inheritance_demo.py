class A:
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")


a1 = A()
a1.feature1()
a1.feature2()


class B(A):    # inherit class A feature into class B
    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")


b1 = B()
b1.feature3()
b1.feature4()


class C(B):    # class C(A,B)  when B is not inherit or A and B are two diff class with diff feature
    def feature5(self):
        print("feature 5 is working")


c1 = C()
c1.feature5()
c1.feature1()