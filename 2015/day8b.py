
input = open("input.txt", "r")

nbc = 0
nbc2 = 0

for line in input:
    nbc = nbc + len(line) - 1
    
    escaped = False
    i = 0
    new_line = "\""
    while i < len(line):
        c = line[i]
        if c == "\"" or c == "\\":
            new_line = new_line + "\\" + c
        elif c != "\n":
            new_line = new_line + c
        i = i + 1
    new_line = new_line + "\""
    nbc2 = nbc2 + len(new_line)

print("Res: ", nbc2 - nbc)

input.close()
