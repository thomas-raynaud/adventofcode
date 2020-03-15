def evalScore(igts, qts):
    '''
    Evaluate the score of the ingredients based on their quantities
    '''
    score = 1
    nameIgts = list(igts.keys())
    nbIgts = len(igts)
    for i in range(4):
        score = score * max(0,
                            sum([igts[nameIgts[x]][i]
                                * qts[x] for x in range(nbIgts)]))
    return score


def getCalories(igts, qts):
    '''
    Get nb of calories of the ingredients based on their quantities
    '''
    nameIgts = list(igts.keys())
    nbIgts = len(igts)
    return sum([igts[nameIgts[x]][4] * qts[x] for x in range(nbIgts)])


def initQts(nbIgts, nbTsIgts, nbTotalTs, qts):
    '''
    Recursive function to create the different possible amounts of igts
    '''
    sumTeaspoons = sum(nbTsIgts)
    if (nbIgts == 1):
        lastTsIgt = nbTotalTs - sum(nbTsIgts)
        qts.append(nbTsIgts + [lastTsIgt])
        return
    for i in range(0, nbTotalTs - sum(nbTsIgts) + 1):
        initQts(nbIgts - 1, nbTsIgts + [i], nbTotalTs, qts)



input = open("input", "r")

igts = dict()

for line in input:
    line = line.replace(',', '')
    args = line.split()
    igts[args[0]] = [int(args[2]), int(args[4]),
                           int(args[6]), int(args[8]), int(args[10])]

nbIgts = len(igts.keys())
qts = []

initQts(nbIgts, [], 100, qts)

scoresP1 = []
scoresP2 = []
for qt in qts:
    score = evalScore(igts, qt)
    scoresP1.append(score)
    if (getCalories(igts, qt) == 500):
        scoresP2.append(score)

print("Best score part 1:", max(scoresP1))
print("Best score part 2:", max(scoresP2))

input.close()
