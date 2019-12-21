program = open('input.txt')
arr = list(map(int, program.read().split(',')))
# arr = program.read().split(',')

# After providing 1 to the only input instruction...
inputs = [1]

# separate an instruction into a sequential list of opscode followed by parameter mode
def parse_instructions(number):
    commands = []
    # add base10 digits, starting with the last 2 digits as the opscode
    commands.append(number % 100)
    number //= 100
    while number:
        commands.append(number % 10)
        number //= 10
    
    # TODO figure out more elegant way to add zeros
    commands.append(0)
    commands.append(0)
    return commands

# def parse_instructions2(number):
#     digits = list(str(number))[::-1]
#     while len(digits)

def execute(mem):
    def add(instructions, i):
        x = mem[mem[i+1]] if instructions[0] == POSITION else mem[i+1]
        y = mem[mem[i+2]] if instructions[1] == POSITION else mem[i+2]

        mem[mem[i+3]] = x + y

    def multiply(instructions, i):
        x = mem[mem[i+1]] if instructions[0] == POSITION else mem[i+1]
        y = mem[mem[i+2]] if instructions[1] == POSITION else mem[i+2]

        mem[mem[i+3]] = x * y

    def output(instructions, i):
        if instructions[0] == POSITION:
            print(mem[mem[i+1]])
        else:
            print(mem[i+1])

    def jump_if_true(instructions, i):
        x = mem[mem[i+1]] if instructions[0] == POSITION else mem[i+1]
        y = mem[mem[i+2]] if instructions[1] == POSITION else mem[i+2]

        if x != 0:
            return y
        else:
            return i+3

    def jump_if_false(instructions, i):
        x = mem[mem[i+1]] if instructions[0] == POSITION else mem[i+1]
        y = mem[mem[i+2]] if instructions[1] == POSITION else mem[i+2]

        if x == 0:
            return y
        else:
            return i+3

    def less_than(instructions, i):
        x = mem[mem[i+1]] if instructions[0] == POSITION else mem[i+1]
        y = mem[mem[i+2]] if instructions[1] == POSITION else mem[i+2]

        if x < y:
            mem[mem[i+3]] = 1
        else:
            mem[mem[i+3]] = 0

    def equals(instructions, i):
        x = mem[mem[i+1]] if instructions[0] == POSITION else mem[i+1]
        y = mem[mem[i+2]] if instructions[1] == POSITION else mem[i+2]

        if x == y:
            mem[mem[i+3]] = 1
        else:
            mem[mem[i+3]] = 0

    # MODES
    POSITION = 0
    IMMEDIATE = 1

    # OPERATIONS
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    END = 99

    i = 0

    while mem[i] != END:
        instructions = parse_instructions(mem[i])
        command = instructions[0]
        print(instructions, command, i)

        if command == ADD:
            add(instructions[1:], i)
            i += 4
        elif command == MULTIPLY:
            multiply(instructions[1:], i)
            i += 4
        elif command == INPUT:
            # take the next input item, add it to position i+1
            mem[mem[i+1]] = inputs.pop(0)
            i += 2
        elif command == OUTPUT:
            output(instructions[1:], i)
            i += 2
        elif command == JUMP_IF_TRUE:
            i = jump_if_true(instructions[1:], i)
        elif command == JUMP_IF_FALSE:
            i = jump_if_false(instructions[1:], i)
        elif command == LESS_THAN:
            less_than(instructions[1:], i)
            i += 4
        elif command == EQUALS:
            equals(instructions[1:], i)
            i += 4
        else:
            print('You gave %s, not valid input' % (mem[i]))



if __name__ == '__main__':
    execute(arr)
