seeds = list()
seeds_to_locations = list()
map_rules = list()

with open("input_d05") as file:
    seeds = [ int(seed) for seed in file.readline().rstrip().split(" ")[1:] ]
    seeds_to_locations = seeds
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

for rules in map_rules:
    for i in range(0, len(seeds_to_locations)):
        for [ dest, source, range_len ] in rules: 
            if seeds_to_locations[i] in range(source, source + range_len):
                seeds_to_locations[i] += dest - source
                break

output = seeds[seeds_to_locations.index(min(seeds_to_locations))]
print(output)
