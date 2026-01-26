def small_greatest(nums):
    largest=nums[0]
    smallest=nums[0]
    for i in nums:
        if i>largest:
            largest=i
        else:
            smallest=i
    return [largest,smallest]
nums=arr = [10, 5, 20, 8, 2]
print(small_greatest(nums))            