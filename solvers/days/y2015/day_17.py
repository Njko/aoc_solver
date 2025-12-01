from aoc_agent.solver import Solver
from itertools import combinations

class DaySolver(Solver):
    def parse(self):
        return [int(line.strip()) for line in self.lines]

    def part1(self) -> "str | int":
        containers = self.parse()
        target = 150
        count = 0
        for i in range(1, len(containers) + 1):
            for c in combinations(containers, i):
                if sum(c) == target:
                    count += 1
        return count

    def part2(self) -> "str | int":
        containers = self.parse()
        target = 150
        
        # Find minimum number of containers
        min_len = float('inf')
        ways_with_min_len = 0
        
        for i in range(1, len(containers) + 1):
            found_at_this_len = 0
            for c in combinations(containers, i):
                if sum(c) == target:
                    found_at_this_len += 1
            
            if found_at_this_len > 0:
                min_len = i
                ways_with_min_len = found_at_this_len
                break # Since we iterate i from 1 upwards, the first time we find any, it's the minimum length
                
        return ways_with_min_len
