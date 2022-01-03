from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)        # for slowdown the machine,


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()
t1.start()              # three thread are there Main thread,t1 thread, t2 thread
sleep(0.2)
t2.start()

t1.join()          # to stop main thread un till t1 and t2 thread execution done
t2.join()
print("Bye")        # the job of main thread
