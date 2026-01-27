def move_zero(arr):
    pos=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[pos]=arr[pos],arr[i]
            pos+=1
    return arr
arr=[1,0,3,2,0,7] 
print(move_zero(arr))       
