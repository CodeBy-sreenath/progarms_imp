n=int(input("enter the number"))
INT_MIN=-2**31
INT_MAX=2**31
sign=-1 if n<0 else 1
n=abs(n) 
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
rev*=sign    
if rev<INT_MIN or rev>INT_MAX:
    print("not valid")  
else:    
      
    print("reverse of the given number is",rev)    