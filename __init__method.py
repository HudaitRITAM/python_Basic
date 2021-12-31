class computer:               # for define a class

    def __init__(self, cpu, ram):            # passing arg assign with these obj
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is", self.cpu, self.ram)


comp1 = computer("i9 intel", 8)             # every object has its own value
comp2 = computer("Ryzen 3", 12)

comp1.config()
comp2.config()


