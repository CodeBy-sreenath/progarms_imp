def median(arr1,arr2):
    merged=arr1+arr2
    merged.sort()
    n=len(merged)
    if n%2==1:
        return merged[n//2]
    else:
        return (merged[n//2]+merged[n//2-1]/2)
arr1=[1,3]
arr2=[2]
print(median(arr1,arr2))    
    