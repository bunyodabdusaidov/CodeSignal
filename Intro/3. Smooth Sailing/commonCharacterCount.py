def solution(s1, s2):
    common = 0 # track the number of common characters
    i = 0 # index of s1
    j = 0 # index of s2
    
    while (True):
        if j >= len(s2): # if the end of s2
            i += 1 # go to the next character in s1
            j = 0 # start over in s2
        
        if i >= len(s1): # if the end of s1
            break # break the loop
        
        if s1[i] == s2[j]: # if common character found
            common += 1 # increment common
            s1 = s1[:i] + s1[i+1:] # delete the common character from s1
            s2 = s2[:j] + s2[j+1:] # delete the common character from s2
            i = 0 # start over in s1
            j = 0 # start over in s2
        
        else: # if common character not found
            j += 1 # go to the next character in s2

    return common

# s1 = "aabcc"
# s2 = "adcaa"
# print(solution(s1,s2))
