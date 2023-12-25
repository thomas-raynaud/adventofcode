c_spelled_out_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
c_spelled_out_numbers_trunc = [number[0:3] for number in c_spelled_out_numbers]

output = 0

for line in open("input_d01"):
    first_digit = ''
    last_digit = ''
    digit = ''
    i = 0
    for char in line:
        if char.isdigit():
            digit = char
        else:
            if any(number in line[i:i+5] for number in c_spelled_out_numbers):
                try:
                    digit = str(c_spelled_out_numbers_trunc.index(line[i:i+3]) + 1)
                except ValueError:
                    pass
        if digit != '':
            if first_digit == '':
                first_digit = digit
            last_digit = digit
        i += 1
    output += int(first_digit + last_digit)

print(output)
