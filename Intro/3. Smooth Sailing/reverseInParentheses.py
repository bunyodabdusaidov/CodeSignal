def solution(inputString):
    output = extract_paren(inputString)

    print(output)

def extract_paren(inputString):
    output = ""
    parens = []
    l = 0
    r = 0
    
    for i in range(len(inputString)):
        if inputString[i] == '(':
            parens.append(i)
        if inputString[i] == ')':
            parens.append(i)
    i = 0
    while i < len(parens):
        org = inputString[:parens[i]]
        print(f"org: {org}")
        rev = inputString[parens[i]+1:parens[i+1]][::-1]
        print(f"rev: {rev}")

        output += org + rev
        print(f"output: {output}")
        i += 2

    
    return output

inputString =  "foo(bar)baz(blim)"
solution(inputString)

