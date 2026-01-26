def swap_array(nums):
    start=0
    end=len(nums)-1
    while start<end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1
    return nums
nums=[1,2,3,4,5]
print(swap_array(nums))    