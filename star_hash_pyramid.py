n=5
for i in range(n):
    for space in range(n-i-1):
        print(" ",end=" ")
    if i%2==0:
        symbol="*"
    else:
        symbol="#"
    for j in range(2*i+1):
        print(symbol,end=" ")
    print()                