def freq_count(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        freq[char]=1
    return freq
s="sreenath"
print(freq_count(s))        
        