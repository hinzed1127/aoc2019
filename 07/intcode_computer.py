from os.path import expanduser
import copy
import itertools


# separate an instruction into a sequential list of opscode followed by parameter mode
def parse_instructions(number):
    commands = []
    # add base10 digits, starting with the last 2 digits as the opscode
    commands.append(number % 100)
    number //= 100
    while number:
        commands.append(number % 10)
        number //= 10
    
    # Tack on extra zeros for commands with less than 2 inputs
    while len(commands) < 3:
        commands.append(0)
    
    return commands

def execute(mem, inputs, startIndex=0):
    # MODES
    POSITION = 0
    # IMMEDIATE = 1

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

    i = startIndex
    output_instruction = None

    while mem[i] != END:
        instructions = parse_instructions(mem[i])
        # print(i, mem[i], instructions)
        command = instructions.pop(0)

        # handle INPUT and OUTPUT separately, as they are always in POSITION mode only
        if command == INPUT:
            # take the next input item, add it to position i+1
            mem[mem[i+1]] = inputs.pop(0)
            i += 2
            continue
        elif command == OUTPUT:
            output_instruction = mem[mem[i+1]]
            # print(output_instruction)
            i += 2
            return (mem, i, output_instruction)
            # continue

        x = mem[mem[i+1]] if instructions[0] == POSITION else mem[i+1]
        y = mem[mem[i+2]] if instructions[1] == POSITION else mem[i+2]

        if command == ADD:
            mem[mem[i+3]] = x + y
            i += 4
        elif command == MULTIPLY:
            mem[mem[i+3]] = x * y
            i += 4
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
    
    return output_instruction
        
def phase_combinations(phase_settings=[]):
    # pt 1
    # phase_settings = [0, 1, 2, 3, 4]
    # ---------------------------------
    # pt 2
    # phase_settings = [5, 6, 7, 8, 9]

    # different syntax, same result
    # combos = [x for x in itertools.permutations(list(range(5)), 5)]
    combos = list(itertools.permutations(phase_settings, len(phase_settings)))
    
    return combos

def amplification_circuit(mem, phase_sequence):
    input_signal = 0
    
    for setting in phase_sequence:
        input_signal = execute(copy.deepcopy(mem), [setting, input_signal])
    
    # the final value of input_signal is the ultimate output
    return input_signal

def feedback_loop(mem, phase_sequence):
    amplifier_series = [copy.deepcopy(mem) for _ in range(5)]
    amplifier_current_indices = [0] * 5
    i = 0 

    # Provide each amplifier its phase setting at its first input instruction;
    # all further input/output instructions are for signals.
    inputs = [phase_sequence.pop(0), 0]
    outputs = []
    while True:
        # if it's not E at the halt code, execute returns (mem, i, output_instruction)
        result = execute(amplifier_series[i], inputs, amplifier_current_indices[i])

        if type(result) == tuple:
            amplifier_series[i], amplifier_current_indices[i], input_signal = result

            if len(phase_sequence) > 0:
                inputs.insert(0, phase_sequence.pop(0))
        
            inputs.append(input_signal)
            # collect outputs for the final result
            outputs.append(input_signal)
        else:
            # halt sequence returns None or final output value, not a tuple
            return outputs[len(outputs)-1]

        i = (i+1) % 5

def find_largest_sequence_output(mem, program, phase_sequence_combinations):
    largest_output_signal = 0

    for phase_sequence in phase_sequence_combinations:
        output_signal = program(copy.deepcopy(mem), list(phase_sequence))
        if output_signal > largest_output_signal:
            largest_output_signal = output_signal
        
    print(largest_output_signal)
    

if __name__ == '__main__':
    program = open(expanduser('~/code/aoc2019/07/input.txt'))
    mem = list(map(int, program.read().split(',')))


    # part 1
    # find_largest_sequence_output(mem, feedback_loop, phase_combinations(list(range(5))))

    # part 2
    find_largest_sequence_output(mem, feedback_loop, phase_combinations(list(range(5, 10))))
        