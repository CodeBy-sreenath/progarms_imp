def vowel_count(s):
    count=0
    arr=[]
    for i in s:
        if i=="A" or i=="E" or i=="I" or i=="O" or i=="U" or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            arr.append(i)
            


            count+=1
    return arr
s="sreenath"
print(vowel_count(s))        