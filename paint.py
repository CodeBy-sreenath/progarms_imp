def can_paint(boards,painters,max_time):
    count=1
    max_sum=0
    for board in boards:
        if max_sum+board<=max_time:
            max_sum=max_sum+board
        else:
            count+=1
            max_sum=board
    if count > painters:
        return False
    return True
def max_paint(board,painters):
    low=max(board)
    high=sum(board)
    result=high
    while low<=high:
        mid=(low+high)//2
        if can_paint(board,painters,mid):
            result=mid
            high=mid-1
        else:    
            low=mid+1
    return result
board=[10,20,30,40]
painters=2
print(max_paint(board,painters))        
        
         
                    