# system
import os
from io import IOBase

# 3rd party
import click

# internal
from days import DayFactory

@click.group(invoke_without_command=True)
@click.option('-d', '--day', required=True, type=click.IntRange(1, 31), metavar="<1..31>", help="Day you want to select.")
@click.option('-p', '--puzzle', required=True, type=click.IntRange(1, 2), metavar="<1|2>", help="Puzzle you want to run.")
@click.option('-i', '--input', required=True, type=click.Path(exists=True), help="Path to puzzle data.")
def cli(day: int, puzzle: int, input: str):
  input_stream = open(os.path.join(input, f"{day:02}_puzzle_{puzzle}.txt"), "r")
  avocd = DayFactory(day, input_stream)

  try:
    avocd.run(puzzle)
  except NotImplementedError:
    print(f"Puzzle {puzzle} for day {day} not implemented.")


if __name__ == "__main__":
  # pylint: disable=no-value-for-parameter
  cli()
