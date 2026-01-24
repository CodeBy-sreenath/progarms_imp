n=int(input("enter the range"))
for i in range(1,n+1):
    for j in range(i):
        if i%2==0:
            print("*",end="")
        else:
            print("#",end="")
    print()            
