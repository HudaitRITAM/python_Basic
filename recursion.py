import sys
sys.setrecursionlimit(1400)     # to set the limit
print(sys.getrecursionlimit())  # print how many time recursion will done

i = 0             # for use as counter


def greet():
    global i
    i += 1
    print("Hello",i)
    greet()


greet()             # function call itself