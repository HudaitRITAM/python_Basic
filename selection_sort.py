# selection sort
def sort(nums):
    for i in range(len(nums)-1):   # len(nums)-1 because index start from 0,
        minpos = i
        for j in range(i, len(nums)):             # for unsorted array range
            if nums[j] < nums[minpos]:
               minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        # print(nums)    # print every iteration


nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print("The sort nums :", nums)