def solution(a, b):
    list_a = []  # Store numbers that are different from list b
    list_b = []  # Store numbers that are different from list a

    for i in range(len(a)):
        # If number in a is not similar with number in b
        if a[i] != b[i]:
            list_a.append(a[i])  # Add number in position i to list_a
            list_b.append(b[i])  # Add number in position i to list_b
    
    # If length of list_a is 0, it means there are no different numbers
    if len(list_a) == 0:
        return True
    # If length of list_a is 2, list_a and list_b should be compared
    elif len(list_a) == 2:
        # Converting list_a and list_b to sets will allow to compare them regardless of their sequence
        return set(list_a) == set(list_b)
    else:
        return False

#a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
#b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
#print(solution(a,b))



