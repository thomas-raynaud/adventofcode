def findReindeerMax(reindeers, param):
    '''
    returns the reindeer maximizing the parameter param
    '''
    listParam = [x[param] for x in reindeers.values()]
    maxParam = max(listParam)
    reindeer = list(reindeers.keys())[listParam.index(maxParam)]
    return reindeer


input = open("input", "r")

timeTravel = 2503

reindeers = dict()

for line in input:
    args = line.split()
    reindeers[args[0]] = { \
                            'speed': int(args[3]), \
                            'tFlying': int(args[6]), \
                            'tResting': int(args[13]), \
                            'nbKm': 0, \
                            'flying': True, \
                            'sCurrState': 0,
                            'score': 0
                         }

for i in range(timeTravel):
    for r in reindeers.values():
        r['sCurrState'] = r['sCurrState'] + 1
        if (r['flying']):
            r['nbKm'] = r['nbKm'] + r['speed']
            if (r['sCurrState'] >= r['tFlying']):
                r['flying'] = False
                r['sCurrState'] = 0
        else:
            if (r['sCurrState'] >= r['tResting']):
                r['flying'] = True
                r['sCurrState'] = 0
        
    # Add bonus for the reindeer in the lead
    rInLead = findReindeerMax(reindeers, 'nbKm') 
    reindeers[rInLead]['score'] = reindeers[rInLead]['score'] + 1


# Find fastest reindeer
winnerP1 = findReindeerMax(reindeers, 'nbKm')
winnerP2 = findReindeerMax(reindeers, 'score')

print("Part One")
print("Winner is", winnerP1, "with", \
      reindeers[winnerP1]['nbKm'],"km covered")

print("Part Two")
print("Winner is", winnerP2, \
      "with a score of", reindeers[winnerP2]['score'])

input.close()
