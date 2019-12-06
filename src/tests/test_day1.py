# system
from io import StringIO

# internal
from ..days.day1 import Day1

def test_puzzle1():
  input_stream = StringIO("\n".join(["12", "14", "1969", "100756"]))

  day = Day1(input_stream)

  result = day.run(1)
  answer = sum([2, 2, 654, 33583])

  assert result == str(answer)

def test_puzzle2():
  input_stream = StringIO("\n".join(["12", "14", "1969", "100756"]))

  day = Day1(input_stream)

  result = day.run(2)
  answer = sum([2, 2, 654, 216, 70, 21, 5, 33583, 11192, 3728, 1240, 411, 135, 43, 12, 2])

  assert result == str(answer)


