input = "1113122113"

counter = 1
val = input[0]
res = ""

for k in range(50):
    counter = 1
    val = input[0]
    res = ""
    for i in range(1, len(input)):
        w = input[i]
        if w == val:
            counter = counter + 1
        else:
            res = res + str(counter) + val
            counter = 1
            val = w
    input = res + str(counter) + val

print(len(input))
