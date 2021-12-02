def solution(a):
    trees = get_trees(a) # trees (-1)
    
    while -1 in a: # remove numbers that equal -1
        a.remove(-1)

    bubble_sort(a) # sort the array (without -1 numbers)

    for i in trees: # insert -1 into its original position in sorted array
        a.insert(i, -1)

    return a

def get_trees(array):
    trees = [] # store trees' index (-1) in original array

    for i in range(len(array)):
        if array[i] == -1: # if number is -1
            trees.append(i) # add its index to trees list
    
    return trees

def bubble_sort(array):
    n = len(array) # array length to iterate through

    for i in range(n):
        sorted = True # flag to stop the array

        for j in range(n - i - 1):
            if array[j] > array[j + 1]: # if number is bigger than its adjacent number
                array[j], array[j + 1] = array[j + 1], array[j] # swap them
                sorted = False # don't finish algorithm prematurely

        if sorted: # if the list is sorted
            break # terminate the loop
    
    return array

#a = [-1, 150, 190, 170, -1, -1, 160, 180]
#print(solution(a))
