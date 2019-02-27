from utility import *


def main(inputFile):
    R, C, F, N, B, T, rides = readInput(inputFile)
    #print(readInput(inputFile))
    assignedRides = set()
    rPriority = setPriority(rides)
    Outputs = setFleet(F, rPriority)
    #print(Outputs)
    exportOutputs(inputFile, Outputs)



if __name__ == "__main__":
    inputFile = "e_high_bonus"
    main(inputFile)