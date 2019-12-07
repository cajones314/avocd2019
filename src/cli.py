# system
from io import IOBase, StringIO
import os


# 3rd party
import click

# internal
from days import DayFactory

# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# logger.addHandler(ch)


@click.group(invoke_without_command=True)
@click.option('-d', '--day', required=True, type=click.IntRange(1, 31), metavar="<1..31>", help="Day you want to select.")
@click.option('-p', '--puzzle', required=True, type=click.IntRange(1, 2), metavar="<1|2>", help="Puzzle you want to run.")
@click.option('-i', '--input', required=True, type=click.Path(exists=True), help="Path to puzzle data.")
def cli(day: int, puzzle: int, input: str):
  filename = os.path.join(input, f"{day:02}_puzzle_{puzzle}.txt")
  if os.path.exists(filename):
    input_stream = open(filename, "r")
  else:
    input_stream = StringIO('')
  avocd = DayFactory(day, input_stream)

  try:
    print(avocd.run(puzzle))
  except NotImplementedError:
    print(f"Puzzle {puzzle} for day {day} not implemented.")


if __name__ == "__main__":
  # pylint: disable=no-value-for-parameter
  cli()
