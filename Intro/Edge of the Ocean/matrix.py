def solution(matrix):
    """
    Track the index of hunted spots and skip the numbers in that index. 
    If the number equals 0, add the index of 0 to hunted set.
    Then, check if the index of number is in the hunted set.
    If the index of number is in hunted set, then skip this number"""
    haunted = set() # track the index of hunted spots (index)
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # if number == 0, add the index of that spot to hunted
            if matrix[i][j] == 0:
                haunted.add(j)
            # if the index of the current spot is in hunted, skip the iteration
            if j in haunted:
                continue
            # else, add the number to total
            else:
                total += matrix[i][j]
    
    return total

#matrix = [[0,1,1,2],[0,5,0,0],[2,0,3,3]]
#print(matrix)
#print(solution(matrix))
