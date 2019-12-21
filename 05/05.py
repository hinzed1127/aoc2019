program = open('input.txt')
arr = list(map(int, program.read().split(',')))

# After providing 1 to the only input instruction...
inputs = [5]

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

def execute(mem):
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
        command = instructions.pop(0)

        x = mem[mem[i+1]] if instructions[0] == POSITION else mem[i+1]

        # add check to avoid index failure on OUTPUT command
        if command != OUTPUT:
            y = mem[mem[i+2]] if instructions[1] == POSITION else mem[i+2]

        if command == ADD:
            mem[mem[i+3]] = x + y
            i += 4
        elif command == MULTIPLY:
            mem[mem[i+3]] = x * y
            i += 4
        elif command == INPUT:
            # take the next input item, add it to position i+1
            mem[mem[i+1]] = inputs.pop(0)
            i += 2
        elif command == OUTPUT:
            print(x)
            i += 2
        elif command == JUMP_IF_TRUE:
            if x != 0:
                i = y
            else:
                i += 3
        elif command == JUMP_IF_FALSE:
            if x == 0:
                i = y
            else:
                i += 3
        elif command == LESS_THAN:
            if x < y:
                mem[mem[i+3]] = 1
            else:
                mem[mem[i+3]] = 0
            i += 4
        elif command == EQUALS:
            if x == y:
                mem[mem[i+3]] = 1
            else:
                mem[mem[i+3]] = 0
            i += 4
        else:
            print('You gave %s, not valid input' % (instructions[0]))
            return
        


if __name__ == '__main__':
    execute(arr)
