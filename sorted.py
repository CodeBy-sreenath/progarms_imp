def sorted(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
nums=[1,2,3,6,5]
print(sorted(nums))    
        