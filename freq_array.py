def freq_array(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
nums=[1,2,1,3,4]
print(freq_array(nums))            