from functools import reduce

times = []
distances = []

with open("input_d06") as file:
    times_file = list(filter(None, file.readline().rstrip().split(" ")))
    distances_file = list(filter(None, file.readline().rstrip().split(" ")))
    for t, d in zip(times_file, distances_file):
        if t.isdigit():
            times.append(int(t))
            distances.append(int(d))

nb_possible_wins_all_races = []
for t, d in zip(times, distances):
    nb_possible_wins = 0
    for x in range(t):
        if (t - x) * x > d:
            nb_possible_wins += 1
    nb_possible_wins_all_races.append(nb_possible_wins)

output = reduce(lambda x, y: x * y, nb_possible_wins_all_races)
print(output)
