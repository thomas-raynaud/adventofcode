input = open("input", "r")

timeTravel = 2503

reindeers = dict()

for line in input:
    args = line.split()
    '''
    Reindeer params:
    - 0: speed
    - 1: time flying
    - 2: time resting
    - 3: nb of km covered
    - 4: state, True = flying, False = resting
    - 5: nb of seconds in current state
    - 6: reindeer score
    '''
    reindeers[args[0]] = [ int(args[3]), int(args[6]), int(args[13]), \
                         0, True, 0, 0 ]

for i in range(timeTravel):
    for n in reindeers.keys():
        speed, tFlying, tResting, \
            nbKm, flying, sCurrState, score = reindeers[n]
        sCurrState = sCurrState + 1
        if (flying):
            nbKm = nbKm + speed
            if (sCurrState >= tFlying):
                flying = False
                sCurrState = 0
        else:
            if (sCurrState >= tResting):
                flying = True
                sCurrState = 0
        
        reindeers[n] = [speed, tFlying, tResting, \
                       nbKm, flying, sCurrState, score]
    
    # Add bonus for the reindeer in the lead
    reindeerInLead = list(reindeers.keys())[0]
    kmReindeerInLead = reindeers[reindeerInLead][3]
    for n in reindeers.keys():
        if (reindeers[n][3] >= kmReindeerInLead):
            reindeerInLead = n
            kmReindeerInLead = reindeers[n][3]
    reindeers[reindeerInLead][6] = reindeers[reindeerInLead][6] + 1


# Find fastest reindeer
winnerP1 = list(reindeers.keys())[0]
winnerP2 = list(reindeers.keys())[0]
maxDistCovered  = reindeers[winnerP1][3]
winnerScore     = reindeers[winnerP2][6]

for n in reindeers.keys():
    if (reindeers[n][3] > maxDistCovered):
        winnerP1 = n
        maxDistCovered = reindeers[n][3]
    if (reindeers[n][6] > winnerScore):
        winnerP2 = n
        winnerScore = reindeers[n][6]

print("Part One")
print("Winner is", winnerP1, "with", maxDistCovered,"km covered")

print("Part Two")
print("Winner is", winnerP2, "with a score of", winnerScore)


input.close()
