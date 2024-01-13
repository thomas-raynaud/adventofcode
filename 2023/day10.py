grid = list()
start_coords = (-1, -1)

for line in open("input_d10"):
    grid.append(list(line.rstrip()))
    if "S" in grid[-1]:
        start_coords = (grid[-1].index("S"), len(grid) - 1)

adj_pipes = [
    [ (-1,  0), [ "-", "L", "F", "S" ] ], # west
    [ ( 1,  0), [ "-", "7", "J", "S" ] ], # east
    [ ( 0, -1), [ "|", "7", "F", "S" ] ], # north
    [ ( 0,  1), [ "|", "L", "J", "S" ] ]  # south
]

path_coords = [ start_coords, None ]
for adj_pipe in adj_pipes:
    cx, cy = [ start_coords[0] + adj_pipe[0][0], start_coords[1] + adj_pipe[0][1] ]
    if grid[cy][cx] in adj_pipe[1]:
        path_coords[1] = (cx, cy)
        break
nb_steps = 1

while path_coords[1] != start_coords:
    prev_coords = path_coords[0]
    o_coords = path_coords[1]
    d_coords = ()
    for adj_pipe in adj_pipes:
        cx, cy = [ o_coords[0] + adj_pipe[0][0], o_coords[1] + adj_pipe[0][1] ]
        try:
            if grid[cy][cx] in adj_pipe[1] and ( cx, cy ) != prev_coords:
                print("A")
                d_coords = (cx, cy)
        except IndexError:
            continue
    print()
    print(d_coords)
    path_coords = [ o_coords, d_coords ]
    nb_steps += 1

output = int(nb_steps / 2)
print(output)
