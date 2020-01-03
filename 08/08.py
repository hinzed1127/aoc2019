pixels = [int(x) for x in open('input.txt').read().strip()]
width = 25
height = 6

# part 1 

layers = []
while len(pixels) > 0:
    layer = []
    for rows in range(height):
        row = []
        for digits in range(width):
            row.append(pixels.pop(0))
        layer.append(row)
    layers.append(layer)

fewest_zeros = 99999
layer_count = {
    'zeros': fewest_zeros,
    'ones': 0,
    'twos': 0
}
for layer in layers:
    zeros = 0
    ones = 0
    twos = 0
    for row in layer:
        for element in row:
            if element == 0:
                zeros += 1
            if element == 1:
                ones += 1
            if element == 2:
                twos += 1
    if zeros < fewest_zeros:
        fewest_zeros = zeros
        layer_count = {
            'zeros': fewest_zeros,
            'ones': ones,
            'twos': twos
        }

print(layer_count)
print(layer_count['ones'] * layer_count['twos'])

# part 2

# initialize an "image" 
image = [[2] * width for _ in range(height)]

for layer in layers:
    for i, row in enumerate(layer):
        for j, element in enumerate(row):
            if image[i][j] == 2:
                image[i][j] = layer[i][j]
                # pixels[i,j] = layer[i][j]
                # print(i,j)

# raw 0s and 1s
for row in image:
    print(''.join(str(x) for x in row))

# "colorized"/decoded image
for row in image:
    print(''.join(str(x).replace('0', '   ').replace('1', '***') for x in row))

