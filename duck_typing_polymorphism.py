
class Pycharm:

    def execute(self):
        print("it compiling")
        print("its running")


class MyEditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("it compiling")
        print("its running")


class Laptop:
    def code(self,ide):               # ide is dynamic typing
        ide.execute()   # duck typing   # so i can replace the type of ide from Pycharm to MyEditor, with
                                 # method execute ,doesn't matter which obj class has been passing ,that obj
                                 # should have execute method


ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)