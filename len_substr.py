def longestsbstr(s):
    char_set=set()
    max_length=0
    left=0
    start=0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        start=left
        max_length=max(max_length,right-left+1)
    return s[start:start+max_length]
s="abcabcabc"
print(longestsbstr(s))        
        