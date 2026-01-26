arr=[1,2,3,4,5]
n=len(arr)
k=2
rotated=arr[-k:]+arr[:-k]
print(rotated)