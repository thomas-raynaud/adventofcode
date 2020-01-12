import sys

def find_dist(c1, c2, roads):
    for road in roads:
        if c1 in road and c2 in road:
            return road[2]

def get_permutations(cities):
    final = [[]]
    l = len(cities)
    groups = [list(cities)] * l
    for i in groups:
        final = [x+[y] for x in final for y in i]
    return final

input = open("input.txt")

cities = []
roads = []

for line in input:
    v1, _, v2, _, dist = line.split()
    if v1 not in cities:
        cities.append(v1)
    if v2 not in cities:
        cities.append(v2)
    roads.append([v1, v2, int(dist)])

proads = get_permutations(cities)

min_dist = sys.maxsize
max_dist = 0

for road in proads:
    dist = 0
    for i in range(1, len(road)):
        dist = dist + find_dist(road[i - 1], road[i], roads)
    min_dist = min(dist, min_dist)
    max_dist = max(dist, max_dist)

print(min_dist, max_dist)

input.close()
