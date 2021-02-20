input = open("input", "r")

msg = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
        }

sue = 1
sueP1 = 0
sueP2 = 0
for line in input:
    args = line.split()
    correctSueP1 = True
    correctSueP2 = True
    charsSue = {
            args[2].replace(":", ""): int(args[3].replace(",", "")),
            args[4].replace(":", ""): int(args[5].replace(",", "")),
            args[6].replace(":", ""): int(args[7])
            }
    # Part 1 check
    for k, v in charsSue.items():
        if msg[k] != v:
            correctSueP1 = False 
    # Part 2 check
    for k, v in charsSue.items():
        if (k in ["cats", "trees"] and msg[k] >= v) \
            or (k in ["pomeranians", "goldfish"] and msg[k] <= v) \
            or (k not in ["pomeranians", "goldfish", "cats", "trees"]
                    and msg[k] != v):
            correctSueP2 = False
    if correctSueP1:
        sueP1 = sue
    if correctSueP2:
        sueP2 = sue
    if correctSueP1 and correctSueP2:
        break
    sue = sue + 1

print("Good Sue Part 1:", sueP1)
print("Good Sue Part 2:", sueP2)

input.close()
