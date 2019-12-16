# system
from io import StringIO

# internal
from ..days.day7 import Day7


def test_puzzle1():
    input1 = [4, 3, 2, 1, 0]
    program1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    answer1 = "43210"
    input2 = [0, 1, 2, 3, 4]
    program2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    answer2 = "54321"
    input3 = [1, 0, 4, 3, 2]
    program3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    answer3 = "65210"

    inputs = [input1, input2, input3]
    programs = [program1, program2, program3]
    answers = [answer1, answer2, answer3]

    for idx, program in enumerate(programs):
        day = Day7(StringIO())
        result = day.run_phases_in_sequence(inputs[idx], program)

        assert result == answers[idx]

def test_puzzle2():
    input1 = [9, 8, 7, 6, 5]
    program1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    answer1 = "139629729"
    input2 = [9, 7, 8, 5, 6]
    program2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    answer2 = "18216"

    inputs = [input1, input2]
    programs = [program1, program2]
    answers = [answer1, answer2]

    for idx, program in enumerate(programs):
        day = Day7(StringIO())
        result = day.run_phases_in_chain(inputs[idx], program)

        assert result == answers[idx]

