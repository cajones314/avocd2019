from os.path import dirname, basename, isfile, join
import glob

# I'm cheating as I don't want to add a new def everytime I add another day.
# Simply doing because I can.
modules = glob.glob(join(dirname(__file__), "day?*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')] 

from .day import Day

def DayFactory(day, input_file):
  #pylint: disable=no-member
  for cls in Day.__subclasses__():
    if cls.__name__ == f"Day{day}":
      return cls(input_file)

  #pylint: disable=not-callable
  return Day(input_file)

from . import *

