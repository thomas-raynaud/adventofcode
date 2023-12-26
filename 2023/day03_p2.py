# Sum of the gear ratios
output = 0

input = []
for line in open("input_d03"):
    input.append(line[:-1])

y = 0
for line in input:
    x = 0
    for char in line:
        if char == '*':
            # Check adjacent cells
            adj_numbers = []
            j = y - 1
            while j <= y + 1:
                i = x - 1
                while i <= x + 1:
                    if (i == x and j == y) or i < 0 or j < 0:
                        i += 1
                        continue
                    try:
                        adj = input[j][i]
                    except IndexError:
                        i += 1
                        continue
                    if adj in '0123456789':
                        # Get complete number ...
                        number = input[j][i]
                        # ... left ...
                        a = i - 1
                        while input[j][a] in '0123456789':
                            number = input[j][a] + number
                            a -= 1
                        # ... and right
                        i += 1
                        try:
                            while input[j][i] in '0123456789':
                                number += input[j][i]
                                i += 1
                        except IndexError:
                            pass
                        adj_numbers.append(int(number))
                    else:
                        i += 1
                j += 1
            if len(adj_numbers) == 2:
                output += adj_numbers[0] * adj_numbers [1]
        x += 1
    y += 1

print(output)
