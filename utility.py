import numpy as np
def readInput(inputFile):
    inputPath = "input\\"+inputFile+".in"
    with open(inputPath, 'r') as data:
        rides = list()
        firstline = data.readline()
        R, C, F, N, B, T = [int(i) for i in firstline.split()]
        for row in data.readlines():
            a, b, x, y, s, f = [int(i) for i in row.split()]
            temp = [(a, b), (x, y), s, f]
            rides.append(temp)

    return R, C, F, N, B, T, rides

def setPriority(rides):
    #for T = 0
    #Urgency tier
    #1 - will end soon
    #2 - Can get Bonus
    #3 - everything else
    #Weights
    #Start time
    #Time to wait if can get bonus

    Riden = 0
    dtype = [('rideN', int), ('priority', int), ('ttt', int), ('st', int)]
    ridePriority = np.array([(i, 0, 0, 0) for i in range(len(rides))], dtype=dtype)
    for ride in rides:
        distanceR = np.subtract(ride[1], ride[0]).sum()
        distanceS = np.array(ride[0]).sum()
        if(ride[3] == distanceR+distanceS):
            ridePriority[Riden]['priority'] = 1
            ridePriority[Riden]['ttt'] = ride[3]-ride[2]
            ridePriority[Riden]['st'] = ride[2]
        elif(ride[2] >= distanceS):
            ridePriority[Riden]['priority'] = 2
            ridePriority[Riden]['ttt'] = ride[3] - ride[2]
            ridePriority[Riden]['st'] = ride[2]
        else:
            ridePriority[Riden]['priority'] = 3
            ridePriority[Riden]['ttt'] = ride[3] - ride[2]
            ridePriority[Riden]['st'] = ride[2]
        Riden += 1
    #sort by priorities
    ridePriority = np.sort(ridePriority, order=['priority', 'st', 'ttt'])
    #print(ridePriority)
    return ridePriority

def setFleet(F, ridePriority):
    Fleet = [[] for i in range(F)]
    Fn = 0
    for ride in ridePriority:
        if Fn == F:
            Fn = 0
        #print(Fn, ride)
        Fleet[Fn].append(ride['rideN'])
        Fn+=1
    return Fleet

def exportOutputs(outputFile, Outputs):
    outputPath = "input\\" + outputFile + ".out"
    with open(outputPath, 'w') as outfile:
        n = 1
        for i in Outputs:
            outfile.write(str(n)+" "+" ".join(map(str, i))+"\n")
            n+=1
