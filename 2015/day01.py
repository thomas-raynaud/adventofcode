f = open('input', 'r')

input = f.read()
floor = 0
basement_char_first_position = -1
for i in range(0, len(input)):
    if input[i] == '(':
        floor += 1
    elif input[i] == ')':
        floor -= 1
        if floor == -1 and  basement_char_first_position == -1:
            basement_char_first_position = i + 1

print("Final floor:", floor)
print("Arrived at basement at position", basement_char_first_position)

f.close()
