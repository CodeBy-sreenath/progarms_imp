def linear_search(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
    return -1
arr=[1,2,3,4,6]
k=3
result=linear_search(arr,k)
print("the element is located at index",result)
