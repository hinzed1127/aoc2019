import re
import math

wires = open('input.txt').readlines()


def wire_coords(wire_path):
    coords = [(0, 0)]
    for instruction in wire_path:
        # https://stackoverflow.com/questions/30933216/split-by-regex-without-resulting-empty-strings-in-python
        direction, magnitude = list(
            filter(None, re.split('(U|D|R|L)', instruction)))
        append_coords(coords, direction, int(magnitude))

    return coords


# add all coordinates in path to a list
def append_coords(coords, direction, magnitude):

    for i in range(magnitude):
        x, y = coords[len(coords) - 1]
        if direction == 'U':
            coords.append((x, y + 1))
        if direction == 'D':
            coords.append((x, y - 1))
        if direction == 'L':
            coords.append((x - 1, y))
        if direction == 'R':
            coords.append((x + 1, y))


# given a list of points where the wires intersect,
# calculate the shortest Manhattan distance from the starting point (origin)
# Manhattan distance = no diagonals, must traverse through a cartesian grid
def shortestManhattanDistance(intersections):
    shortest = math.inf
    for point in intersections:
        x, y = point
        distance = abs(x) + abs(y)
        if (distance == 0):
            # exclude the starting point for both
            continue
        elif (distance < shortest):
            shortest = distance

    print(shortest)


def fewestCombinedSteps(path1, path2, intersections):
    fewestSteps = math.inf

    for point in intersections:
        path1_index = path1.index(point)
        path2_index = path2.index(point)
        steps = path1_index + path2_index
        if (steps == 0):
            # exclude the starting point for both
            continue
        elif (steps < fewestSteps):
            fewestSteps = steps

    print(fewestSteps)


wire_a = wire_coords(wires[0].strip().split(','))
wire_b = wire_coords(wires[1].strip().split(','))
intersections = set(wire_a).intersection(set(wire_b))

# part 1
shortestManhattanDistance(intersections)

# part 2
fewestCombinedSteps(wire_a, wire_b, intersections)
