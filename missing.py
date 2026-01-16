def missing_num(arr,n):
    total=n*(n+1)//2
    arr_sum=sum(arr)
    missing=total-arr_sum
    print("missing number is",missing)
arr=[1,3,4,5,6]
n=6
missing_num(arr,n)

