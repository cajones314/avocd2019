# system
from io import StringIO

# internal
from ..days.day3 import Day3

def test_puzzle1():
    problem1 = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
    answer1  = '6'
    problem2 = ["R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83"]
    answer2  = '159'
    problem3 = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
    answer3  = '135'

    problems = [problem1, problem2, problem3]
    answers  = [answer1,  answer2,  answer3]

    for idx, problem in enumerate(problems):
        input_stream = StringIO("\n".join(problem))
        day = Day3(input_stream)

        result = day.run(1)
        answer = answers[idx]

        assert result == answer

def test_puzzle2():
    problem1 = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
    answer1  = '30'
    problem2 = ["R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83"]
    answer2  = '610'
    problem3 = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
    answer3  = '410'

    problems = [problem1, problem2, problem3]
    answers  = [answer1,  answer2,  answer3]

    for idx, problem in enumerate(problems):
        input_stream = StringIO("\n".join(problem))
        day = Day3(input_stream)

        result = day.run(2)
        answer = answers[idx]

        assert result == answer

