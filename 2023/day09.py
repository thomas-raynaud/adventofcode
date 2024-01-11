output_p1 = 0
output_p2 = 0

for line_str in open("input_d09"):
    line = [ int(x) for x in line_str.rstrip().split(" ") ]
    all_deltas = list()
    deltas_all_zero = False
    prev_deltas = line
    all_deltas.append(line)
    while not deltas_all_zero:
        deltas_all_zero = True
        deltas = list()
        for i in range(0, len(prev_deltas) - 1):
            delta = prev_deltas[i + 1] - prev_deltas[i]
            deltas.append(delta)
            if delta != 0:
                deltas_all_zero = False
        all_deltas.append(deltas)
        prev_deltas = deltas

    all_deltas[-1].append(0)
    for i in range(len(all_deltas) - 2, -1, -1):
        all_deltas[i].append(all_deltas[i][-1] + all_deltas[i + 1][-1])
        # Part 2
        all_deltas[i].insert(0, all_deltas[i][0] - all_deltas[i + 1][0])

    output_p1 += all_deltas[0][-1]
    output_p2 += all_deltas[0][0]

print(output_p1)
print(output_p2)
