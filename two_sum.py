def two_sum(arr,target):
    dic={}
    for i,num in enumerate(arr):
        complement=target-num
        if complement in dic:
            return [dic[complement],i]
        else:
            dic[num]=i
arr=[2,7,11,15] 
target=9
print(two_sum(arr,target))           