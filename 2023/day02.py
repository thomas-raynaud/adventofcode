c_max_red = 12
c_max_green = 13
c_max_blue = 14

# Sum of the IDs of the games
output_part_1 = 0
# Sum of the power of the minimum sets of cubes
output_part_2 = 0
id_ind = 1

for line in open("input_d02"):
    game_rounds = line.split(":")[1].split(";")
    game_possible = True
    min_red = 0
    min_green = 0
    min_blue = 0
    for game_round in game_rounds:
        nb_red = 0
        nb_green = 0
        nb_blue = 0
        for color_pick in game_round.split(","):
            color_pick_args = color_pick.split(" ")
            nb_color = int(color_pick_args[1])
            if color_pick_args[2][0] == 'r':
                nb_red = nb_color
                min_red = max(min_red, nb_color)
            elif color_pick_args[2][0] == 'g':
                nb_green = nb_color
                min_green = max(min_green, nb_color)
            else:
                nb_blue = nb_color
                min_blue = max(min_blue, nb_color)
            if nb_red > c_max_red or nb_green > c_max_green or nb_blue > c_max_blue:
                game_possible = False
                # break -> don´t break out of loop for part 2
        # if not game_possible:
            # break -> don´t break out of loop for part 2
    if game_possible:
        output_part_1 += id_ind
    output_part_2 += (min_red * min_green * min_blue)
    id_ind += 1

print("Part 1 :" + str(output_part_1))
print("Part 2 :" + str(output_part_2))
