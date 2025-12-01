from aoc_agent.solver import Solver

class DaySolver(Solver):
    """
    Solves Day 1: Not Quite Lisp
    
    Approach:
    - Part 1: Iterate through the input string. Increment floor for '(', decrement for ')'. Return final floor.
    - Part 2: Same iteration, but stop and return the 1-based index when floor reaches -1.
    """
    def part1(self) -> "str | int":
        floor = 0
        for char in self.input_data:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
        return floor

    def part2(self) -> "str | int":
        floor = 0
        for i, char in enumerate(self.input_data, 1):
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            
            if floor == -1:
                return i
        return "Never reached basement"
