def second_largest(n):
    largest=float('-inf')
    second=float('-inf')
    for i in n:
        if i>largest:
            second=largest
            largest=i
        elif i>second and i!=largest:
            second=i
    return second
n=[12,2,4,5,6]
print(second_largest(n))            