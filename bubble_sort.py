 # Bubble sort
def sort(nums):
    for i in range(len(nums)-1,0,-1): # len(nums)-1 because index start from 0, -1 since go for negetive order
        for j in range(i):             # after every iteration we get a fix value
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [14, 400, 48, 97, 34, 78]
sort(nums)
print("The sort nums :", nums)