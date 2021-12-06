def solution(inputString):
    parens = []
    i = 0
    
    # if there are no parentheses, return the input itself
    if '(' and ')' not in inputString:
        return inputString

    # else if input consists of only '(' and ')', return an empty string
    elif '(' and ')' in inputString and len(inputString) == 2:
        return ""

    # else, loop through the string, and reverse strings in parentheses
    else:
        # repeat until there are no parentheses left
        while '(' and ')' in inputString:
            # add matching parentheses to `parens` list
            if inputString[i] == '(':
                parens = [i]
            if inputString[i] == ')':
                parens.append(i)
                
                # get the beginning of original string
                begin = inputString[:parens[0]]
                # get the word in parentheses
                rev_word = inputString[parens[0]+1:parens[1]]
                # get the remaining string
                end = inputString[parens[1]+1:]
                # concatinate beginning, reversed word, and end of string
                inputString = begin + rev_word[::-1] + end
                # set i = 0 to start the loop again and check for any parentheses
                i = 0
            # if parentheses not found, increment i
            else:
                i += 1
                # if i reaches the end of string, break the loop
                if i >= len(inputString):
                    break
    
    return inputString

#inputString = "foo(barzab)blim"
#print(solution(inputString))
