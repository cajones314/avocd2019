# system
import math
from enum import Enum
from pprint import pprint

# 3rd party
import numpy as np 

# internal
from .day import Day

"""
===============================================================================
Day 2 Puzzle 1

On the way to your gravity assist around the Moon, your ship computer beeps
angrily about a "1202 program alarm". On the radio, an Elf is already
explaining how to handle the situation: "Don't worry, that's perfectly norma--"
The ship computer bursts into flames.

You notify the Elves that the computer's magic smoke seems to have escaped.
"That computer ran Intcode programs like the gravity assist program it was
working on; surely there are enough spare parts up there to build a new Intcode
computer!"

An Intcode program is a list of integers separated by commas (like 1,0,0,3,99).
To run one, start by looking at the first integer (called position 0). Here,
you will find an opcode - either 1, 2, or 99. The opcode indicates what to do;
for example, 99 means that the program is finished and should immediately halt.
Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result in
a third position. The three integers immediately after the opcode tell you
these three positions - the first two indicate the positions from which you
should read the input values, and the third indicates the position at which the
output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the
values at positions 10 and 20, add those values, and then overwrite the value
at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs
instead of adding them. Again, the three integers after the opcode indicate
where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward
4 positions.

For example, suppose you have the following program:

1,9,10,3,2,3,11,0,99,30,40,50 For the purposes of illustration, here is the
same program split into multiple lines:

1,9,10,3, 2,3,11,0, 99, 30,40,50 The first four integers, 1,9,10,3, are at
positions 0, 1, 2, and 3. Together, they represent the first opcode (1,
addition), the positions of the two inputs (9 and 10), and the position of the
output (3). To handle this opcode, you first need to get the values at the
input positions: position 9 contains 30, and position 10 contains 40. Add these
numbers together to get 70. Then, store this value at the output position;
here, the output position (3) is at position 3, so it overwrites itself.
Afterward, the program looks like this:

1,9,10,70, 2,3,11,0, 99, 30,40,50 Step forward 4 positions to reach the next
opcode, 2. This opcode works just like the previous, but it multiplies instead
of adding. The inputs are at positions 3 and 11; these positions contain 70 and
50 respectively. Multiplying these produces 3500; this is stored at position 0:

3500,9,10,70, 2,3,11,0, 99, 30,40,50 Stepping forward 4 more positions arrives
at opcode 99, halting the program.

Here are the initial and final states of a few more small programs:

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2). 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2
= 6). 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99. Once you have a working
computer, the first step is to restore the gravity assist program (your puzzle
input) to the "1202 program alarm" state it had just before the last computer
caught fire. To do this, before running the program, replace position 1 with
the value 12 and replace position 2 with the value 2. What value is left at
position 0 after the program halts?

"""

class IntcodeComputer:
    # Program counter
    _pc  = 0

    # Computer running flag
    _run = True

    def __init__(self, memory: list):
        self._memory = memory

    @property
    def memory(self):
        return self._memory

    def _add(self, r1: int, r2: int, r3: int) -> None:
        x, y = self.memory[r1], self.memory[r2]
        self.memory[r3] =  x + y
    
    def _mul(self, r1: int,  r2: int, r3: int) -> None:
        x, y = self.memory[r1], self.memory[r2]
        self.memory[r3] = x * y

    def _hlt(self, x, y, r3) -> None:
        self._run = False

    class Opcodes(Enum):
        ADD = 1
        MUL = 2
        HLT = 99

    # Defining lookup table for opcode -> function
    _func_table = {
        Opcodes.ADD: _add,
        Opcodes.MUL: _mul,
        Opcodes.HLT: _hlt
    }

    # Pull a word at a time out of memory
    def _get_word(self, pc):
        return self.memory[pc:pc+4]

    def execute(self):
        while self._run:
            word = self._get_word(self._pc)

            # Ensure we grabbed a full word
            if len(word) == 4:
                opcode, r1, r2, r3 = word
                self._func_table[IntcodeComputer.Opcodes(opcode)].__call__(self, r1, r2, r3)
                self._pc += 4
            # Not a full word left in computer, so Halt
            else: 
                self._func_table[IntcodeComputer.Opcodes.HLT].__call__(self, 0, 0, 0)

        return self.memory


class Day2(Day):
    def _run_intcode_program(self, program: list):
        computer = IntcodeComputer(program)

        return computer.execute()

    def _puzzle1(self):
        answer = ''

        # read program name from first line
        program_name = self._input_stream.readline()
        program_name = program_name.strip()

        # apparently pylint doesn't know about 3.8 iteralbes on streams
        # pylint: disable=not-an-iterable
        for line in self._input_stream:
            # remove whitespace, split on commas, and convert to ints
            program = line.strip()
            program = program.split(',')
            program = [int(x) for x in program]

            # per context rules change these memory positions
            if program_name == "1202 program alarm":
                program[1] = 12
                program[2] = 2
                result = self._run_intcode_program(program)
                result = [ result[0] ]
            else:
                result = self._run_intcode_program(program)

            answer = ",".join([ str(x) for x in result ])

        return str(answer)
