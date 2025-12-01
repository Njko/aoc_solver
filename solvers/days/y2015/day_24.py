from aoc_agent.solver import Solver
from itertools import combinations
import math

class DaySolver(Solver):
    def parse(self):
        return [int(line.strip()) for line in self.lines]

    def solve_balance(self, weights, groups):
        total_weight = sum(weights)
        target_weight = total_weight // groups
        
        # We need to find the smallest group 1 that sums to target_weight
        # Iterate length from 1 upwards
        for length in range(1, len(weights)):
            qes = []
            for c in combinations(weights, length):
                if sum(c) == target_weight:
                    # Calculate QE
                    qe = math.prod(c)
                    qes.append(qe)
            
            if qes:
                return min(qes)
        return -1

    def part1(self) -> "str | int":
        weights = self.parse()
        return self.solve_balance(weights, 3)

    def part2(self) -> "str | int":
        weights = self.parse()
        return self.solve_balance(weights, 4)
