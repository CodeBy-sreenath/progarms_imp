def longest_prefix(s):
    if not s:
        return ""
    prefix=s[0]
    for word in s[1:]:
        while not word.startswith(prefix):
            
            prefix=prefix[:-1]
            if prefix=="":
                return ""
    return prefix

print(longest_prefix(["flower","flow","flight"]))        
            