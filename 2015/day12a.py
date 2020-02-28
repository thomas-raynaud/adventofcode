import json

def get_sum(data):
    sum = 0
    if isinstance(data, dict):
        for element in data:
            sum = sum + get_sum(data[element])
    elif isinstance(data, list):
        for element in data:
            sum = sum + get_sum(element)
    else:
        sum = 0 if not isinstance(data, int) else data
    return sum

input = open("input", "r")
data = json.load(input)
print("sum: ", get_sum(data))

input.close()
