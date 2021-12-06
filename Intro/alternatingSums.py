def solution(a):
    team1 = []  #store team1
    team2 = []  #store team2

    for i in range(len(a)):
        n = i + 1  #increase index by one to check if it's even or odd number
        #if index is even, add the number at this index to team2 list
        if n % 2 == 0:  
            team2.append(a[i])
        #if index is odd, add the number at this index to team1 list
        else:
            team1.append(a[i])
    #create list containing sum of both teams
    output = [sum(team1), sum(team2)]
    return output

#a = [50, 60, 60, 45, 70]
#print(solution(a))

