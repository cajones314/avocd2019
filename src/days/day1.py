from io import IOBase
from .day import Day

class Day1(Day):
  def _puzzle1(self):
    # apparently pylint doesn't know about 3.8 iteralbes on streams 
    #pylint: disable=not-an-iterable
    for line in self._input_stream:
      line = line.rstrip("\n")
      print(f"Line: {line}")

    return "done."

  def _puzzle2(self):
    return "puzzle2"
