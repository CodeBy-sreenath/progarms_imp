def duplicate(s):
    seen=set()
    char=''
    for i in s:
        if i not in seen:
            char+=i
            seen.add(i)
    return char
s="sreenath"
print(duplicate(s))        