import sys

sys.setrecursionlimit(50000)

adj_pipes = [
    [ (-1,  0), [ "-", "7", "J", "S" ], [ "-", "L", "F", "S" ] ], # west
    [ ( 1,  0), [ "-", "L", "F", "S" ], [ "-", "7", "J", "S" ] ], # east
    [ ( 0, -1), [ "|", "L", "J", "S" ], [ "|", "7", "F", "S" ] ], # north
    [ ( 0,  1), [ "|", "7", "F", "S" ], [ "|", "L", "J", "S" ] ]  # south
]

def progress_in_path(objective_coords, prev_coords, curr_coords, grid):
    if objective_coords == curr_coords:
        return 1
    else:
        for adj_pipe in adj_pipes:
            cx, cy = [ curr_coords[0] + adj_pipe[0][0], curr_coords[1] + adj_pipe[0][1] ]
            try:
                if grid[curr_coords[1]][curr_coords[0]] in adj_pipe[1] and grid[cy][cx] in adj_pipe[2] and ( cx, cy ) != prev_coords:
                    length_path = progress_in_path(objective_coords, curr_coords, (cx, cy), grid)
                    if length_path != -1:
                        return length_path + 1
            except IndexError:
                continue
        # No path found to reach objective
        return -1

grid = list()
start_coords = (-1, -1)

for line in open("input_d10"):
    grid.append(list(line.rstrip()))
    if "S" in grid[-1]:
        start_coords = (grid[-1].index("S"), len(grid) - 1)

path_coords = [ start_coords, None ]
for adj_pipe in adj_pipes:
    cx, cy = [ start_coords[0] + adj_pipe[0][0], start_coords[1] + adj_pipe[0][1] ]
    if grid[cy][cx] in adj_pipe[2]:
        length_path = progress_in_path(start_coords, start_coords, (cx, cy), grid)
        break
nb_steps = 1

output = int(length_path / 2)
print(output)
