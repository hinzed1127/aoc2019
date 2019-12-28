from os.path import expanduser
import intcode_computer
import unittest

class KnownValues(unittest.TestCase):
    known_values = (
        ('test_signal_43210.txt', [4,3,2,1,0], 43210),
        ('test_signal_54321.txt', [0,1,2,3,4], 54321),
        ('test_signal_65210.txt', [1,0,4,3,2], 65210)
    )

    feedback_loop_values = (
        ('test_signal_139629729.txt', [9,8,7,6,5], 139629729),
        ('test_signal_18216.txt', [9,7,8,5,6], 18216)
    )

    def test_amplification_circuit(self):
        '''amplication_circuit should give known result with known input'''
        for file, phase_sequence, output_signal in self.known_values:
            intcode_program = open(expanduser('~/code/aoc2019/07/%s' % file))
            mem = list(map(int, intcode_program.read().split(',')))

            result = intcode_computer.amplification_circuit(mem, phase_sequence)
            self.assertEqual(output_signal, result)

    def test_feedback_loop(self):
        '''feedback_loop should give known result with known input'''
        for file, phase_sequence, output_signal in self.feedback_loop_values:
            intcode_program = open(expanduser('~/code/aoc2019/07/%s' % file))
            mem = list(map(int, intcode_program.read().split(',')))

            result = intcode_computer.feedback_loop(mem, phase_sequence)
            self.assertEqual(output_signal, result)

if __name__ == '__main__':
    unittest.main()
