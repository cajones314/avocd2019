import math

from .day import Day

"""
===============================================================================
Day 1 Puzzle 1
Fuel required to launch a given module is based on its mass. Specifically, to 
find the fuel required for a module, take its mass, divide by three, round 
down, and subtract 2.


===============================================================================
Day 1 Puzzle 2
During the second Go / No Go poll, the Elf in charge of the Rocket Equation 
Double-Checker stops the launch sequence. Apparently, you forgot to include 
additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, 
round down, and subtract 2. However, that fuel also requires fuel, and that 
fuel requires fuel, and so on. Any mass that would require negative fuel should
instead be treated as if it requires zero fuel; the remaining mass, if any, is 
instead handled by wishing really hard, which has no mass and is outside the 
scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, 
treat the fuel amount you just calculated as the input mass and repeat the 
process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel 
(2 divided by 3 and rounded down is 0, which would call for a negative fuel), 
so the total fuel required is still just 2. At first, a module of mass 1969 
requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 
then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, 
which requires no further fuel. So, the total fuel required for a module of 
mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.

The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 
+3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

What is the sum of the fuel requirements for all of the modules on your 
spacecraft when also taking into account the mass of the added fuel? 
(Calculate the fuel requirements for each module separately, then add them 
all up at the end.)
"""    

class Day1(Day):
  def _get_fuel_for_mass(self, mass: int):
    result = math.floor(mass/3) - 2
    # no such thing as negative fuel
    if result < 0:
      result = 0

    return result

  def _get_fuel_for_fuel(self, fuel: int):
    result = 0

    additional_fuel = fuel
    while (additional_fuel := self._get_fuel_for_mass(additional_fuel)) != 0:
      result += additional_fuel

    return result

  def _puzzle1(self):
    answer = 0
    
    # apparently pylint doesn't know about 3.8 iteralbes on streams
    # pylint: disable=not-an-iterable
    for line in self._input_stream:
      mass = int(line.rstrip("\n"))      
      answer += self._get_fuel_for_mass(mass)

    return str(answer)

  def _puzzle2(self):
    answer = 0
    
    # apparently pylint doesn't know about 3.8 iteralbes on streams
    # pylint: disable=not-an-iterable
    for line in self._input_stream:
      mass = int(line.rstrip("\n"))      
      fuel = self._get_fuel_for_mass(mass)
      additional_fuel = self._get_fuel_for_fuel(fuel)
      answer = answer + fuel + additional_fuel

    return str(answer)
