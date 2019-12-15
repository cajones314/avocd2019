# system
from io import StringIO

# internal
from ..days.day6 import Day6


def test_puzzle1():
    problem = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"]
    answer = "42"

    input_stream = StringIO("\n".join(problem))
    day = Day6(input_stream)
    result = day.run(1)

    assert result == answer

def test_puzzle2():
    problem = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L", "K)YOU", "I)SAN"]
    answer = "4"

    input_stream = StringIO("\n".join(problem))
    day = Day6(input_stream)
    result = day.run(2)

    assert result == answer
