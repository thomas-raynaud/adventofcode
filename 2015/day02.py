f = open('input', 'r')
wp_amount = 0
ribbon_amount = 0
for line in f:
    if line == '\n':
        continue
    dims = [int(i) for i in line.split('x')]
    dims.sort()
    ribbon_amount += 2 * dims[0] + 2 * dims[1] + dims[0] * dims[1] * dims[2]
    wp_amount += 3 * dims[0] * dims[1] + 2 * dims[1] * dims[2] + 2 * dims[2] * dims[0]
print("Square feet of wrapping paper:", wp_amount)
print("Feet of ribbon:", ribbon_amount)
