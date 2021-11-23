def solution(statues):
    needed = 0
    for i in range(len(statues) - 1):
        for j in range(len(statues) - 1):
            j = i + 1
            if statues[i] > statues[j]:
                temp = statues[j]
                statues[j] = statues[i]
                statues[i] = temp
                i = 0
    print(statues)
    for i in range(len(statues) - 1):
        if statues[i+1] - statues[i] != 1:
            needed += (statues[i+1] - 1) - (statues[i])
    return needed
