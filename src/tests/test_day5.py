# system
from io import StringIO

# 3rd party
import pytest

# internal
from ..days.day5 import Day5


def test_puzzle2(capsys):

    input1 = "8"
    program1 = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    answer1 = "1"

    input2 = "8"
    program2 = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    answer2 = "0"

    input3 = "7"
    program3 = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    answer3 = "1"

    input4 = "8"
    program4 = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    answer4 = "1"

    input5 = "5"
    program5 = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    answer5 = "1"

    input6 = "0"
    program6 = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    answer6 = "0"

    input7 = "1243"
    program7 = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    answer7 = "1"

    input8 = "3"
    program8 = [
        3,
        21,
        1008,
        21,
        8,
        20,
        1005,
        20,
        22,
        107,
        8,
        21,
        20,
        1006,
        20,
        31,
        1106,
        0,
        36,
        98,
        0,
        0,
        1002,
        21,
        125,
        20,
        4,
        20,
        1105,
        1,
        46,
        104,
        999,
        1105,
        1,
        46,
        1101,
        1000,
        1,
        20,
        4,
        20,
        1105,
        1,
        46,
        98,
        99,
    ]
    answer8 = "999"

    input9 = "8"
    program9 = [
        3,
        21,
        1008,
        21,
        8,
        20,
        1005,
        20,
        22,
        107,
        8,
        21,
        20,
        1006,
        20,
        31,
        1106,
        0,
        36,
        98,
        0,
        0,
        1002,
        21,
        125,
        20,
        4,
        20,
        1105,
        1,
        46,
        104,
        999,
        1105,
        1,
        46,
        1101,
        1000,
        1,
        20,
        4,
        20,
        1105,
        1,
        46,
        98,
        99,
    ]
    answer9 = "1000"

    input10 = "3323"
    program10 = [
        3,
        21,
        1008,
        21,
        8,
        20,
        1005,
        20,
        22,
        107,
        8,
        21,
        20,
        1006,
        20,
        31,
        1106,
        0,
        36,
        98,
        0,
        0,
        1002,
        21,
        125,
        20,
        4,
        20,
        1105,
        1,
        46,
        104,
        999,
        1105,
        1,
        46,
        1101,
        1000,
        1,
        20,
        4,
        20,
        1105,
        1,
        46,
        98,
        99,
    ]
    answer10 = "1001"

    inputs = [
        input1,
        input2,
        input3,
        input4,
        input5,
        input6,
        input7,
        input8,
        input9,
        input10,
    ]
    programs = [
        program1,
        program2,
        program3,
        program4,
        program5,
        program6,
        program7,
        program8,
        program9,
        program10,
    ]
    answers = [
        answer1,
        answer2,
        answer3,
        answer4,
        answer5,
        answer6,
        answer7,
        answer8,
        answer9,
        answer10,
    ]

    for idx, program in enumerate(programs):
        input_stream = StringIO(f"{inputs[idx]}\n" + ",".join([str(x) for x in program]) + "\n")
        day = Day5(input_stream)
        _ = day.run(2)
        answer = answers[idx]
        captured = capsys.readouterr()

        assert captured.out.strip() == answer
