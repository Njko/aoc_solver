from aoc_agent.solver import Solver
import re

class DaySolver(Solver):
    def parse(self):
        # "To continue, please consult the code grid in the manual.  Enter the code at row 2978, column 3083."
        match = re.search(r"row (\d+), column (\d+)", self.input_data)
        if match:
            return int(match.group(1)), int(match.group(2))
        return 0, 0

    def part1(self) -> "str | int":
        row, col = self.parse()
        
        # Calculate the index in the sequence
        # Diagonal number D = row + col - 1
        # Number of items in full diagonals before D is T(D-1) = (D-1)*D/2
        # Index in current diagonal is col
        # Total index n = T(D-1) + col
        
        d = row + col - 1
        n = (d * (d - 1)) // 2 + col
        
        # We need the (n-1)-th number in the sequence (since 1st is start_code)
        # code = start_code * (multiplier ^ (n-1)) % modulus
        
        start_code = 20151125
        multiplier = 252533
        modulus = 33554393
        
        code = (start_code * pow(multiplier, n - 1, modulus)) % modulus
        return code

    def part2(self) -> "str | int":
        return "Merry Christmas!"
