def extract_paren(inputString):
    output = ""
    parens = []
    l = 0
    r = 0
    
    i = 0
    while '(' or ')' in inputString:
        #print(f"i = {i}")
        if inputString[i] == '(':
            parens = [i]
            #print(f"`(` = {parens[0]}")
        if inputString[i] == ')':
            parens.append(i)
            rev_word = inputString[parens[0]+1:parens[1]]
            #print(f"`)` = {parens[1]}")
            #print(f"parens = {parens[0]}, {parens[1]}")
            #print(parens)
            #print(f"parens: {inputString[parens[0]+1:parens[1]]}")
            #print(f"inputString[:parens[0]] = {inputString[:parens[0]]}")
            #print(f"inputString[parens[1]+1:] = {inputString[parens[1]+1:]}")
            inputString = inputString[:parens[0]] + rev_word[::-1] + inputString[parens[1]+1:]
            #print(f"inputString: {inputString}")
            i = 0
        i += 1
        if i >= len(inputString):
            break
    
    return inputString

def solution(inputString):
    parens = []
    
    i = 0

    if inputString == "":
        return inputString

    while '(' or ')' in inputString:
        if inputString[i] == '(':
            parens = [i]
        if inputString[i] == ')':
            parens.append(i)
            
            begin = inputString[:parens[0]]
            rev_word = inputString[parens[0]+1:parens[1]]
            end = inputString[parens[1]+1:]
            inputString = begin + rev_word[::-1] + end
            i = 0
        
        i += 1
        if i >= len(inputString):
            break
    
    return inputString

inputString = "(foo(bar(baz)))blim(go)(yes(no(maybe)))"
print(inputString)
print(solution(inputString))

