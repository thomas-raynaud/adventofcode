from PIL import Image
import numpy as np

def to_img(lights):
    brightness_max = np.amax(lights)
    rescaled = ((255 * lights) / brightness_max).astype(np.uint8)
    img = Image.fromarray(rescaled).save("lightsb.jpg")

input = open("input.txt", "r")
lights = np.zeros((1000, 1000))
for instruction in input:
    brightness_var = 2
    ins_w = instruction.split()
    offset = 0
    if ins_w[0] == "turn":
        if ins_w[1] == "off":
            brightness_var = -1
        else:
            brightness_var = 1
        offset = 1
    x1, y1 = [int(x) for x in ins_w[1 + offset].split(",")]
    x2, y2 = [int(x) + 1 for x in ins_w[3 + offset].split(",")]

    lights[x1:x2, y1:y2] = lights[x1:x2, y1:y2] + brightness_var
    lights[x1:x2, y1:y2][np.where(lights[x1:x2, y1:y2] < 0)] = 0   

nb_lights_on = int(np.sum(lights))
print("Nb lights on: ", nb_lights_on)

to_img(lights)

input.close()
