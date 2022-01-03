
pos = -1


def search(list, n):
    i = 0

    while i < len(list):              # linear search using while loop
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1

    return False

#   for i in range(len(list)):        # linear search using for loop
#        if list[i] == n:
#            print('found at pos', i+1)
#            break
#    else:
#        print('not found')


list = [91, 62, 43, 47, 85, 10]
n = int(input("Enter the number for found :"))

if search(list,n):
    print("yes,it's here at", pos+1)
else:
    print("sorry,not found")
