from io import IOBase

"""Base class for the individual day puzzles"""
class Day:
  def __init__(self, input_stream: IOBase):
      self._input_stream = input_stream
    
  def _puzzle1(self):
    raise NotImplementedError

  def _puzzle2(self):
    raise NotImplementedError

  def run(self, puzzle: int):
    if puzzle == 1:
      return self._puzzle1()
    elif puzzle == 2:
      return self._puzzle2()
    else:
      raise NotImplementedError

