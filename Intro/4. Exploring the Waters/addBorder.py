def solution(picture):
    output = []  # output list
    
    # loop through strings in picture array
    for string in picture:
        border = "*" + string + "*"  # add asterisk (*) to beginning and end of string
        output.append(border)  # add the modified string to output list

    output.insert(0, "*" * len(output[0]))  # insert only asterisk (*) string to the beginning of the output array 
    output.append("*" * len(output[0]))  # append only asterisk (*) string to the end of the output array

    return output

#picture = ["abc", "ded"]
#print(solution(picture))
