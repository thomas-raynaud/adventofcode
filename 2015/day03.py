import sets

input = open('input', 'r').read()
santa_position_step1 = {'x': 0, 'y': 0}
santa_position_step2 = {'x': 0, 'y': 0}
robot_position = {'x': 0, 'y': 0}
location_set_step1 = set([(0, 0)])
location_set_step2 = set([(0, 0)])
movement_dict = {
        '^': (lambda position: {'x': position['x'], 'y': position['y'] + 1}),
        'v': (lambda position: {'x': position['x'], 'y': position['y'] - 1}),
        '>': (lambda position: {'x': position['x'] + 1, 'y': position['y']}),
        '<': (lambda position: {'x': position['x'] - 1, 'y': position['y']})
}

for i in range(0, len(input)):
    if input[i] in movement_dict.keys():
        if(i % 2 == 0):
            santa_position_step2 = movement_dict[input[i]](santa_position_step2)
            location_set_step2.add((santa_position_step2['x'], santa_position_step2['y']))
        else:
            robot_position = movement_dict[input[i]](robot_position)
            location_set_step2.add((robot_position['x'], robot_position['y']))
        santa_position_step1 = movement_dict[input[i]](santa_position_step1)
        location_set_step1.add((santa_position_step1['x'], santa_position_step1['y']))
print('Step 1: ', len(location_set_step1))
print('Step 2: ', len(location_set_step2))
