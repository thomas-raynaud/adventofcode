import functools, math

network = dict()
locs_p2 = []

def get_nb_end_locs(locs):
    return len([ x for x in locs_p2 if x[-1:] == "Z" ])


def is_end_loc(end_loc, is_part_1=True):
    return end_loc == "ZZZ" or (not is_part_1 and end_loc[-1:] == "Z")


def get_nb_steps(loc, network, is_part_1=True):
    nb_steps = 0
    while not is_end_loc(loc, is_part_1):
        for instruction in instructions:
            if instruction == "L":
                loc = network[loc][0]
            else:
                loc = network[loc][1]
            nb_steps += 1
            if is_end_loc(loc, is_part_1):
                break
    return nb_steps


with open("input_d08") as file:
    instructions = file.readline().rstrip()
    file.readline()
    line = file.readline()
    while line != "":
        args_line = []
        for arg in line.split(" "):
            args_line.append("".join([ x for x in arg if x.isalpha() or x.isdigit() ]))
        parent, _, left, right = args_line
        network[parent] = (left, right)
        if parent[-1:] == "A":
            locs_p2.append(parent)
        line = file.readline()

# Output part 1
print(get_nb_steps("AAA", network))

nb_steps_per_path = []

for loc in locs_p2:
    nb_steps_per_path.append(get_nb_steps(loc, network, is_part_1=False))

output_p2 = functools.reduce(lambda a,b : math.lcm(a,b), nb_steps_per_path)
print(output_p2)
