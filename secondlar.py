def second_largest(nums):
    first_largest=float('-inf')
    second_largest=float('-inf')
    for i in nums:
        if i>first_largest:
            second_largest=first_largest
            first_largest=i
        elif i>second_largest and i!=first_largest:
            second_largest=i
    return second_largest
nums=[1,3,6,7,9]
print(second_largest(nums))            