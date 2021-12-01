def solution(n):
    number = str(n) # convert to string to get the length of number
    half = len(number) // 2 # get the half of the number (middle)
    first_half = 0 # first half of the integer
    second_half = 0 # second half of the integer
    for n in number[:half]: # calculate the sum of the first half of number
        first_half += int(n)
    for n in number[half:]: # calculate the sum of the second half of number
        second_half += int(n)
    if first_half == second_half: # check first and second half are equal
        return True # if equal, return true
    else:
        return False # if not, return false

#n = 1230
#print(solution(n))
