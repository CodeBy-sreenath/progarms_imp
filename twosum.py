def two_sum(s,target):
    dic={}
    for i,num in enumerate(s):
        dif=target-num
        if dif in dic:
            return [dic[dif],i]
        else:
            dic[num]=i
    return []
s=[2,7,11,15]
target=9
print(two_sum(s,target))        