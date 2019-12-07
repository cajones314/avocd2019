# system
from io import StringIO

# internal
from ..days.day2 import Day2

def test_puzzle1():
  program1 = [1,0,0,0,99]
  answer1  = [2,0,0,0,99]
  program2 = [2,3,0,3,99]
  answer2  = [2,3,0,6,99]
  program3 = [2,4,4,5,99,0]
  answer3  = [2,4,4,5,99,9801]
  program4 = [1,1,1,4,99,5,6,0,99]
  answer4  = [30,1,1,4,2,5,6,0,99]
  program5 = [1,9,10,3,2,3,11,0,99,30,40,50]
  answer5  = [3500,9,10,70,2,3,11,0,99,30,40,50]

  programs = [program1, program2, program3, program4, program5]
  answers  = [answer1,  answer2,  answer3,  answer4, answer5]

  for idx, program in enumerate(programs):
    input_stream = StringIO("test_program\n" + ",".join([ str(x) for x in program ]) + "\n")
    day = Day2(input_stream)
    result = day.run(1)
    answer = ",".join([ str(x) for x in answers[idx] ])
    assert result == answer

def test_puzzle2():
  pass
