def second_largest(arr):
    largest=float('-inf')
    second=float('-inf')
    for num in arr:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=largest:
            second=num
    return second
arr=[1,2,34,78,21]
print(second_largest(arr))        
