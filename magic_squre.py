def magic_squre(n):
    if n%2==0:
        print("magic squre is work for only odd values of n")
        return
    squre=[[0]*n for _ in range(n)]
    i=0
    j=n//2
    for num in range(1,n*n+1):
        squre[i][j]=num
        new_i=(i-1)%n
        new_j=(j+1)%n
        if squre[new_i][new_j]!=0:
            i=(i+1)%n
        else:
            i=new_i
            j=new_j
    for row in squre:
        print(*row)
    return 
(magic_squre(3))                    