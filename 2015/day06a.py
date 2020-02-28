from PIL import Image
import numpy as np

def to_img(lights):
    rescaled = (255 * lights).astype(np.uint8)
    img = Image.fromarray(rescaled).save("lights.jpg")

input = open("input", "r")
lights = np.zeros((1000, 1000))
for instruction in input:
    switch_type = 2
    ins_w = instruction.split()
    offset = 0
    if ins_w[0] == "turn":
        if ins_w[1] == "off":
            switch_type = 0
        else:
            switch_type = 1
        offset = 1
    x1, y1 = [int(x) for x in ins_w[1 + offset].split(",")]
    x2, y2 = [int(x) + 1 for x in ins_w[3 + offset].split(",")]

    if switch_type == 2:
        lights[x1:x2, y1:y2] = np.logical_not(lights[x1:x2, y1:y2])
    else:
        lights[x1:x2, y1:y2] = switch_type


nb_lights_on = int(np.sum(lights))
print("Nb lights on: ", nb_lights_on)

to_img(lights)

input.close()
