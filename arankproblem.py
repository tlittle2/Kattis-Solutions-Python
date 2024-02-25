def main():
    teams, games = list(map(int, input().split()))

    teamsList = [i for i in range(1,teams+1)]

    for i in range(games):
        winner,loser = list(map(str, input().split()))

        winner = int(winner[1:len(winner)])
        loser = int(loser[1:len(loser)])

        if teamsList.index(loser) < teamsList.index(winner):
            tempList = list()

            if(teamsList.index(loser) !=0):
                for element in range(0, teamsList.index(loser)):
                    tempList.append(teamsList[element])


            for element in range(teamsList.index(loser)+1, teamsList.index(winner)+1):
                tempList.append(teamsList[element])

            tempList.append(teamsList[teamsList.index(loser)])


            for element in range(tempList.index(loser)+1, len(teamsList)):
                tempList.append(teamsList[element])

            teamsList = tempList


    
    for i in teamsList:
        print("T{}".format(i), end=" ")

    





if __name__ == "__main__":
    main()
