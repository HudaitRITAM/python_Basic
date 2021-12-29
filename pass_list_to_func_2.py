# Take  names from users,how many user want and count and display the number of names that have
# name length bigger than 5 letters.
# this program is to check the number of user inputs having len of 5 or more than
lst = []
n = int(input('enter the size of the list: '))
for i in range(0,n):
    name = input("Enter names :")
    lst.append(name)

namelist = []
def count(lst):

    counter = 0
    for r in lst:
        if len(r) > 5:
            namelist.append(r)
            counter += 1
        else:
            continue

    return counter, namelist

counter , namelist = count(lst)

print('The number of names {} and list {}'.format(counter,namelist))