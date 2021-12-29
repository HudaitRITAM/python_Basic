

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd

lst = [12,23,35,67,78,9,98,24,56,7,82,56,76]

even, odd = count(lst)

print("Even : {} and Odd : {}".format(even,odd))
