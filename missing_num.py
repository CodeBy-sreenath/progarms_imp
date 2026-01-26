def missing(num):
    n=len(num)
    sum1=(n+1)*(n+1+1)//2
    sum2=sum(num)
    missing_num=sum1-sum2
    return missing_num
num=[1,2,3,5]
print(missing(num))