# make sure value are already sorted in binary search

pos = -1


def search(list, n):
    l = 0
    u = len(list)-1

    while l <= u:              # binary search using while loop
        mid = (l+u) // 2       # integer division
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1      # already before mid-value is checked
            else:
                u = mid - 1      # have to skip that  mid- value
    return False


list = [10, 25, 32, 47, 49, 58, 62, 66, 88, 93, 145, 1122, 1245, 1589, 12456]
n = int(input("Enter the number for found :"))

if search(list,n):
    print("yes,it's here at", pos+1)
else:
    print("sorry,not found")
