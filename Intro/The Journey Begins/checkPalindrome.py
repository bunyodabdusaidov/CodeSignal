def solution(inputString):
    str_len = len(inputString) - 1
    is_palindrome = True
    for s in range(len(inputString)//2+1):
        if inputString[s] != inputString[str_len]:
            is_palindrome = False
            break
        str_len -= 1
    return is_palindrome
