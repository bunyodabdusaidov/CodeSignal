def solution(inputArray):
    str_max_size = 0 # track the size of the longest string
    
    if len(inputArray) == 1: # if array has only one string, return the array
        return inputArray
    
    # get the maximum length of the string
    for i in range(len(inputArray)):
        if len(inputArray[i]) > str_max_size:
            str_max_size = len(inputArray[i])
    
    outputArray = [] # array to store the strings with maximum size
    # store only strings with the maximum size
    for string in inputArray:
        if len(string) == str_max_size:
            outputArray.append(string)
    
    return outputArray

#inputArray = ["aba", "aa", "ad", "vcd", "aba"]
#print(solution(inputArray))
