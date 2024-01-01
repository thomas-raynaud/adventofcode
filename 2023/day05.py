import numpy as np

def convert_seeds_to_locations(seeds, map_rules):
    locations = seeds
    for rules in map_rules:
        for i in range(0, len(locations)):
            for [ dest, source, range_len ] in rules: 
                if locations[i] in range(source, source + range_len):
                    locations[i] += dest - source
                    break
    return locations

seeds_p1 = list()
seeds_ranges_p2 = list()
map_rules = list()

with open("input_d05") as file:
    seeds_p1 = [ int(seed) for seed in file.readline().rstrip().split(" ")[1:] ]
    seeds_ranges_p2 = np.resize(seeds_p1, (int(len(seeds_p1)/2), 2)).tolist()
    rules = []
    for line in file:
        if line[0] == "\n":
            continue
        elif line[0].isdigit():
            rules.append([ int(val) for val in line.rstrip().split(" ")])
        else:
            if rules:
                map_rules.append(rules)
                rules = []
    map_rules.append(rules)

locations_p1 = convert_seeds_to_locations(seeds_p1, map_rules)

# Part 2: too many seeds to process. So best option is to check out for locations starting at #0
# and find of the seeds to plant.
loc_ind = 0
seed_found = False
inv_map_rules = map_rules[::-1]
for rules in map_rules:
    for rule in rules:
        tmp = rule[0]
        rule[0] = rule[1]
        rule[1] = tmp

step = 10000
while not seed_found:
    seed = convert_seeds_to_locations([ loc_ind ], inv_map_rules)[0]
    for [ seeds_start, seeds_len ] in seeds_ranges_p2:
        if seed in range(seeds_start, seeds_start + seeds_len):
            seed_found = True
            break
    if not seed_found:
        loc_ind += step
    elif step > 1: # Sharpen the step to reach the correct location
        loc_ind -= step
        step = int(step / 10)
        seed_found = False

output_p1 = seeds_p1[locations_p1.index(min(locations_p1))]
output_p2 = loc_ind
print(output_p1)
print(output_p2)
