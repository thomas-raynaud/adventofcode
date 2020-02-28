from itertools import permutations

input = open("input", "r")

relations = dict()
attendees = []

for line in input:
    args = line.split()
    n1 = args[0]
    v = int(args[3])
    if (args[2] == "lose"):
        v = -v
    n2 = args[10]
    n2 = n2[:-1] # Remove the point (end of sentence)
    if (n1 not in attendees):
        attendees.append(n1)
        relations[(n1, "Me")] = 0
        relations[("Me", n1)] = 0
    relations[(n1, n2)] = v

attendees.append("Me")

max_happiness = -666
best_config = []

for config in permutations(attendees):
    # Testing a configuration
    happiness = 0
    for i in range(len(config)):
        at1 = config[i]
        at2 = config[(i + 1) % len(config)]
        happiness = happiness + relations[(at1, at2)] + relations[(at2, at1)]
    # Check if it is the best configuraton
    if (happiness > max_happiness):
        max_happiness = happiness
        best_config = config

print("Best arrangement:", best_config)
print("Happiness:", max_happiness)

input.close()
