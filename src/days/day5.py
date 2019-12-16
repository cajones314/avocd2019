# system
import math
from enum import Enum
from itertools import product
from io import StringIO
from typing import List

# 3rd party

# internal
from .day import Day

"""
===============================================================================
Day 5 Puzzle 1

You're starting to sweat as the ship makes its way toward Mercury. The Elves
suggest that you get the air conditioner working by upgrading your ship
computer to support the Thermal Environment Supervision Terminal.

The Thermal Environment Supervision Terminal (TEST) starts by running a
diagnostic program (your puzzle input). The TEST diagnostic program will run on
your existing Intcode computer after a few modifications:

First, you'll need to add two new instructions:

Opcode 3 takes a single integer as input and saves it to the position given by
its only parameter. For example, the instruction 3,50 would take an input value
and store it at address 50. Opcode 4 outputs the value of its only parameter.
For example, the instruction 4,50 would output the value at address 50.
Programs that use these instructions will come with documentation that explains
what should be connected to the input and output. The program 3,0,4,0,99
outputs whatever it gets as input, then halts.

Second, you'll need to add support for parameter modes:

Each parameter of an instruction is handled based on its parameter mode. Right
now, your ship computer already understands parameter mode 0, position mode,
which causes the parameter to be interpreted as a position - if the parameter
is 50, its value is the value stored at address 50 in memory. Until now, all
parameters have been in position mode.

Now, your ship computer will also need to handle parameters in mode 1,
immediate mode. In immediate mode, a parameter is interpreted as a value - if
the parameter is 50, its value is simply 50.

Parameter modes are stored in the same value as the instruction's opcode. The
opcode is a two-digit number based only on the ones and tens digit of the
value, that is, the opcode is the rightmost two digits of the first value in an
instruction. Parameter modes are single digits, one per parameter, read
right-to-left from the opcode: the first parameter's mode is in the hundreds
digit, the second parameter's mode is in the thousands digit, the third
parameter's mode is in the ten-thousands digit, and so on. Any missing modes
are 0.

For example, consider the program 1002,4,3,4,33.

The first instruction, 1002,4,3,4, is a multiply instruction - the rightmost
two digits of the first value, 02, indicate opcode 2, multiplication. Then,
going right to left, the parameter modes are 0 (hundreds digit), 1 (thousands
digit), and 0 (ten-thousands digit, not present and therefore zero):

ABCDE 1002

DE - two-digit opcode,      02 == opcode 2 C - mode of 1st parameter,  0 ==
position mode B - mode of 2nd parameter,  1 == immediate mode A - mode of 3rd
parameter,  0 == position mode, omitted due to being a leading zero This
instruction multiplies its first two parameters. The first parameter, 4 in
position mode, works like it did before - its value is the value stored at
address 4 (33). The second parameter, 3 in immediate mode, simply has value 3.
The result of this operation, 33 * 3 = 99, is written according to the third
parameter, 4 in position mode, which also works like it did before - 99 is
written to address 4.

Parameters that an instruction writes to will never be in immediate mode.

Finally, some notes:

It is important to remember that the instruction pointer should increase by the
number of values in the instruction after the instruction finishes. Because of
the new instructions, this amount is no longer always 4. Integers can be
negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, store the result
in position 4). The TEST diagnostic program will start by requesting from the
user the ID of the system to test by running an input instruction - provide it
1, the ID for the ship's air conditioner unit.

It will then perform a series of diagnostic tests confirming that various parts
of the Intcode computer, like parameter modes, function correctly. For each
test, it will run an output instruction indicating how far the result of the
test was from the expected value, where 0 means the test was successful.
Non-zero outputs mean that a function is not working correctly; check the
instructions that were run before the output instruction to see which one
failed.

Finally, the program will output a diagnostic code and immediately halt. This
final output isn't an error; an output followed immediately by a halt means the
program finished. If all outputs were zero except the diagnostic code, the
diagnostic program ran successfully.

After providing 1 to the only input instruction and passing all the tests, what
diagnostic code does the program produce?


===============================================================================
Day 5 Puzzle 2

The air conditioner comes online! Its cold air feels good for a while, but then
the TEST alarms start to go off. Since the air conditioner can't vent its heat
anywhere but back into the spacecraft, it's actually making the air inside the
ship warmer.

Instead, you'll need to use the TEST to extend the thermal radiators.
Fortunately, the diagnostic program (your puzzle input) is already equipped for
this. Unfortunately, your Intcode computer is not.

Your computer is only missing a few opcodes:

Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the
instruction pointer to the value from the second parameter. Otherwise, it does
nothing. Opcode 6 is jump-if-false: if the first parameter is zero, it sets the
instruction pointer to the value from the second parameter. Otherwise, it does
nothing. Opcode 7 is less than: if the first parameter is less than the second
parameter, it stores 1 in the position given by the third parameter. Otherwise,
it stores 0. Opcode 8 is equals: if the first parameter is equal to the second
parameter, it stores 1 in the position given by the third parameter. Otherwise,
it stores 0. Like all instructions, these instructions need to support
parameter modes as described above.

Normally, after an instruction is finished, the instruction pointer increases
by the number of values in that instruction. However, if the instruction
modifies the instruction pointer, that value is used and the instruction
pointer is not automatically increased.

For example, here are several programs that take one input, compare it to the
value 8, and then produce one output:

3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is
equal to 8; output 1 (if it is) or 0 (if it is not). 3,9,7,9,10,9,4,9,99,-1,8 -
Using position mode, consider whether the input is less than 8; output 1 (if it
is) or 0 (if it is not). 3,3,1108,-1,8,3,4,3,99 - Using immediate mode,
consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is
not). 3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input
is less than 8; output 1 (if it is) or 0 (if it is not). 

Here are some jump tests that take an input, then output 0 if the input was zero
or 1 if the input was non-zero:

3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode) Here's a larger
example:

3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99 The above example program
uses an input instruction to ask for a single number. The program will then
output 999 if the input value is below 8, output 1000 if the input value is
equal to 8, or output 1001 if the input value is greater than 8.

This time, when the TEST diagnostic program runs its input instruction to get
the ID of the system to test, provide it 5, the ID for the ship's thermal
radiator controller. This diagnostic test suite only outputs one number, the
diagnostic code.

What is the diagnostic code for system ID 5?
"""

class IntcodeComputer:
    # Program counter
    _pc = 0

    # Computer running flag
    _run = True

    def __init__(self, memory: list, input_stream: StringIO):
        self._memory = memory
        self._input_stream = input_stream

    @property
    def memory(self):
        return self._memory

    def _add(self, param1: int, param2: int) -> None:
        r1, r2, r3 = self._read_registers(3)

        x = self._read_memory(r1, param1)
        y = self._read_memory(r2, param2)

        self.memory[r3] = x + y

    def _mul(self, param1: int, param2: int) -> None:
        r1, r2, r3 = self._read_registers(3)

        x = self._read_memory(r1, param1)
        y = self._read_memory(r2, param2)

        self.memory[r3] = x * y

    def _inp(self, param1: int, param2: int) -> None:
        r1 = (self._read_registers(1))[0]

        val = int(self._input_stream.readline().strip())
        self.memory[r1] = val

    def _out(self, param1: int, param2: int) -> None:
        r1 = (self._read_registers(1))[0]
        
        x = self._read_memory(r1, param1)

        print(str(x))

    # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the
    # instruction pointer to the value from the second parameter. Otherwise, it does
    # nothing. 
    def _jnz(self, param1: int, param2: int) -> None:
        r1, r2 = self._read_registers(2)

        x = self._read_memory(r1, param1)
        pc = self._read_memory(r2, param2)

        if x != 0:
            self._pc = pc

    # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the
    # instruction pointer to the value from the second parameter. Otherwise, it does
    # nothing. 
    def _jez(self, param1: int, param2: int) -> None:
        r1, r2 = self._read_registers(2)

        x = self._read_memory(r1, param1)
        pc = self._read_memory(r2, param2)

        if x == 0:
            self._pc = pc

    # Opcode 7 is less than: if the first parameter is less than the second
    # parameter, it stores 1 in the position given by the third parameter. Otherwise,
    # it stores 0. 
    def _clt(self, param1: int, param2: int) -> None:
        r1, r2, r3 = self._read_registers(3)

        x = self._read_memory(r1, param1)
        y = self._read_memory(r2, param2)

        if x < y:
            self.memory[r3] = 1
        else:
            self.memory[r3] = 0

    # Opcode 8 is equals: if the first parameter is equal to the second
    # parameter, it stores 1 in the position given by the third parameter. Otherwise,
    # it stores 0. Like all instructions, these instructions need to support
    # parameter modes as described above.
    def _ceq(self, param1: int, param2: int) -> None:
        r1, r2, r3 = self._read_registers(3)

        x = self._read_memory(r1, param1)
        y = self._read_memory(r2, param2)

        if x == y:
            self.memory[r3] = 1
        else:
            self.memory[r3] = 0


    def _hlt(self, param1: int, param2: int) -> None:
        self._run = False


    class Opcodes(Enum):
        ADD = 1
        MUL = 2
        INP = 3
        OUT = 4
        JNZ = 5
        JEZ = 6
        CLT = 7
        CEQ = 8
        HLT = 99

    # Defining lookup table for opcode -> function
    _func_table = {
        Opcodes.ADD: _add,
        Opcodes.MUL: _mul,
        Opcodes.INP: _inp,
        Opcodes.OUT: _out,
        Opcodes.JNZ: _jnz,
        Opcodes.JEZ: _jez,
        Opcodes.CLT: _clt,
        Opcodes.CEQ: _ceq,
        Opcodes.HLT: _hlt
    }

    # Pull a word at a time out of memory
    def _read_opcode(self):
        val = self.memory[self._pc]
        opcode = val % 100
        param1 = int(val := val / 100) % 10
        param2 = int(val := val / 10) % 10
    
        self._pc += 1

        return (opcode, param1, param2)

    def _read_registers(self, count):
        registers = self.memory[self._pc : self._pc + count]
        self._pc += count
        return registers

    def _read_memory(self, register, parameter):
        if parameter:
            val = register
        else:
            val = self.memory[register]
        return val

    def execute(self):
        while self._run:
            opcode, param1, param2 = self._read_opcode()
            
            self._func_table[IntcodeComputer.Opcodes(opcode)].__call__(
                self, param1, param2
            )

        return self.memory


class Day5(Day):
    def _run_intcode_program(self, program: list, input_stream: StringIO):
        memory = []

        if program is not None:
            computer = IntcodeComputer(program, input_stream)

            memory = computer.execute()

        return memory

    def _read_program(self) -> (str, List[int]):
        program = None

        input_string = self._input_stream.readline()

        # apparently pylint doesn't know about 3.8 iteralbes on streams
        # pylint: disable=not-an-iterable
        for line in self._input_stream:
            # remove whitespace, split on commas, and convert to ints
            program = line.strip()
            program = program.split(",")
            program = [int(x) for x in program]

        return (input_string, program)

    def _puzzle1(self):
        answer = ""

        input_string, program = self._read_program()
        input_stream = StringIO(input_string)
        # per context rules change these memory positions
        _ = self._run_intcode_program(program, input_stream)

        return str(answer)

    def _puzzle2(self):
        answer = ""

        input_string, program = self._read_program()
        input_stream = StringIO(input_string)
        # per context rules change these memory positions
        _ = self._run_intcode_program(program, input_stream)

        return str(answer)
