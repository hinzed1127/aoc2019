import copy
program = open('input.txt')
arr = list(map(int, program.read().split(',')))


def add(mem, x, y, output):
    mem[output] = mem[x] + mem[y]


def multiply(mem, x, y, output):
    mem[output] = mem[x] * mem[y]


def execute(mem, noun, verb):
    i = 0
    mem[1] = noun
    mem[2] = verb

    while mem[i] != 99:
        if mem[i] == 1:
            add(mem, mem[i+1], mem[i+2], mem[i+3])
        elif mem[i] == 2:
            multiply(mem, mem[i+1], mem[i+2], mem[i+3])
        else:
            print('Not 1 or 2, something went wrong')
        i += 4

    return mem[0]


target = 19690720
for i in range(100):
    for j in range(100):
        array = copy.deepcopy(arr)
        if execute(array, i, j) == 19690720:
            print(i, j)
            break
