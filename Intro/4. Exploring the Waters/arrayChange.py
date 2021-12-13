def solution(inputArray):
    count = 0  # Count number of moves
    for i in range(len(inputArray) - 1):
        if inputArray[i + 1] <= inputArray[i]:
            add = inputArray[i] - inputArray[i + 1] + 1  # Compute the difference and add one
            inputArray[i + 1] += add  # Update the array
            count += add  # Update the count
    return count

#inputArray = [1,1,1]
#print(solution(inputArray))
