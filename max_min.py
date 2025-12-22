def large_min(n):
    large=n[0]
    min=n[0]
    for i in range(1,len(n)):
        if n[i]>large:
            large=n[i]
        if n[i]<min:
            min=n[i]
    return large,min
    
n=[1,4,5,8,0]
print(large_min(n))        