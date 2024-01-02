from functools import reduce
from math import sqrt, floor, ceil

times = []
distances = []
time_p2 = ""
distance_p2 = ""

with open("input_d06") as file:
    times_file = list(filter(None, file.readline().rstrip().split(" ")))
    distances_file = list(filter(None, file.readline().rstrip().split(" ")))
    for t, d in zip(times_file, distances_file):
        if t.isdigit():
            times.append(int(t))
            distances.append(int(d))
            time_p2 += t
            distance_p2 += d

nb_possible_wins_all_races = []
for t, d in zip(times, distances):
    nb_possible_wins = 0
    root_1 = (-t + sqrt(pow(t, 2) - 4 * d)) / -2
    root_2 = (-t - sqrt(pow(t, 2) - 4 * d)) / -2
    nb_possible_wins = (ceil(root_2) - floor(root_1)) - 1
    nb_possible_wins_all_races.append(nb_possible_wins)

output = reduce(lambda x, y: x * y, nb_possible_wins_all_races)
print(output)

# Part 2
time_p2 = int(time_p2)
distance_p2 = int(distance_p2)

root_1 = (-time_p2 + sqrt(pow(time_p2, 2) - 4 * distance_p2)) / -2
root_2 = (-time_p2 - sqrt(pow(time_p2, 2) - 4 * distance_p2)) / -2

output = (ceil(root_2) - floor(root_1)) - 1
print(output)
