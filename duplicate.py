def duplicate(s):
    char=[]
    seen=set()
    for i in s:
        if i in seen:
            char.append(i)
        else:
            seen.add(i)
    return seen
s="sreenath"
print(duplicate(s))            