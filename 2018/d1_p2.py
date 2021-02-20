freqs = {0: True}
freq = 0
f = open("input_d1", "r")
found = False
while True:
    f.seek(0)
    for l in f:
        freq += int(l)
        if freq in freqs:
            found = True
            break
        freqs[freq] = True
    if found:
        print freq
        break
