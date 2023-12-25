# Sum of the part numbers
output = 0
c_input_file_name = "input_d03"

# First loop through input: find part numbers and store coordinates to check for adjacent symbols
positions_to_check = [] # Tuple : (part_number, [ array_of_coordinates_to_check ])
input = []
y = 0 # line number
for line in open(c_input_file_name):
    x = 0 # char number in line
    reading_number = False
    input.append(line[:-1]) # Don´t keep the line return at the end of the line
    number_x_positions = []
    for char in line:
        if reading_number:
            if char.isdigit():
                number += char
                number_x_positions.append(x)
            else:
                reading_number = False
                # Number is read. Compute coordinates to check
                coordinates_to_check = []
                i = 0
                for x_pos in number_x_positions:
                    if i == 0:
                        coordinates_to_check.append((x_pos - 1, y - 1))
                        coordinates_to_check.append((x_pos - 1, y + 1))
                        coordinates_to_check.append((x_pos - 1, y))
                        coordinates_to_check.append((x_pos, y - 1))
                        coordinates_to_check.append((x_pos, y + 1))
                    if i == len(number_x_positions) - 1:
                        coordinates_to_check.append((x_pos + 1, y))
                    coordinates_to_check.append((x_pos + 1, y - 1))
                    coordinates_to_check.append((x_pos + 1, y + 1))
                    i += 1
                positions_to_check.append((int(number), coordinates_to_check))
                number_x_positions = []
        else:
            if char.isdigit():
                number = char
                number_x_positions.append(x)
                reading_number = True
        x += 1
    y += 1

# Check if part numbers are adjacent to a symbol
for part_number, coordinates_arr_to_check in positions_to_check:
    for x, y in coordinates_arr_to_check:
        try:
            char = input[y][x]
        except IndexError:
            continue
        if x < 0 or y < 0:
            continue
        if not char.isdigit() and char != '.':
            output += part_number
            break

print(output)
