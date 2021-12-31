
class computer:               # for define a class
    def config(self):         # define a method which actually func
        print("16gb RAM,550gb SSD,i9 core Processor")


comp1 = computer()             # make object with the help of class
comp2 = computer()

# computer.config(comp1)            # calling config and passing comp1
# computer.config(comp2)

comp1.config()             # method config use comp1 as parameter as self object
comp2.config()


