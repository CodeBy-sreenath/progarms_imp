n=5
for i in range(n):
    for j in range(n - i- 1):
        print(" ",end=" ")
    for space in range(2*i+1):
        print("*",end=" ")
    print()    
for i in range(n-2,0,-1):
    for j in range(n-i-1):
        
        print(" ",end=" ")
    for s in range(2*i-1):
        print("*",end=" ")
    print()        
            