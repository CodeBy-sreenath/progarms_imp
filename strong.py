n=int(input("enter the number"))
temp=n
sum=0

while n>0:
    fact=1
    r=n%10
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if sum==temp:
    print("strong number")
else:
    print("not a strong number")        