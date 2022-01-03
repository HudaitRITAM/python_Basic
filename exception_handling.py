a = 5
b = 0

try:                # at least try once run or not
    print("resource open")
    print(a/b)
    k = int(input("Enter a number :"))
    print(k)
except ZeroDivisionError as e:       # exception handling
    print("you can not divide by zero", e)
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("Something went wrong..")

finally:              # finally block will be executed if we get error as well as if we don't get the error
    print("resource closed")