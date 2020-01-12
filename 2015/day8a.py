
input = open("input.txt", "r")

nbc = 0
nbm = 0

for line in input:
    nbc = nbc + len(line) - 1
    
    escaped = False
    i = 0
    while i < len(line):
        c = line[i]
        if not escaped:
            if c == "\\":
                escaped = True
            elif c != "\"" and c != "\n":
                nbm = nbm + 1
        else:
            escaped = False
            nbm = nbm + 1
            if c == "x":
                i = i + 2
        i = i + 1

print("Res: ", nbc - nbm)

input.close()
