output_p1 = 0
output_p2 = 0

for line_str in open("input_d09"):
    line = [ int(x) for x in line_str.rstrip().split(" ") ]
    all_deltas = list()
    deltas_all_zero = False
    all_deltas.append(line)
    while not deltas_all_zero:
        deltas_all_zero = True
        deltas = list()
        for i in range(0, len(all_deltas[-1]) - 1):
            deltas.append(all_deltas[-1][i + 1] - all_deltas[-1][i])
            deltas_all_zero = deltas_all_zero and deltas[-1] == 0
        all_deltas.append(deltas)

    for i in range(len(all_deltas) - 2, -1, -1):
        all_deltas[i].append(all_deltas[i][-1] + all_deltas[i + 1][-1])
        all_deltas[i].insert(0, all_deltas[i][0] - all_deltas[i + 1][0])

    output_p1 += all_deltas[0][-1]
    output_p2 += all_deltas[0][0]

print(output_p1)
print(output_p2)
