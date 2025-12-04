from solvers.solver import Solver
import itertools

class Day02Solver(Solver):
    def part1(self) -> "str | int":
        total_sum = 0
        lines = self.input_data.strip().split('\n')
        
        for line in lines:
            if not line.strip():
                continue
            # Handle both tab and space separated values
            parts = line.replace('\t', ' ').split()
            nums = [int(x) for x in parts]
            if not nums:
                continue
                
            total_sum += max(nums) - min(nums)
            
        return total_sum

    def part2(self) -> "str | int":
        total_sum = 0
        lines = self.input_data.strip().split('\n')
        
        for line in lines:
            if not line.strip():
                continue
            parts = line.replace('\t', ' ').split()
            nums = [int(x) for x in parts]
            if not nums:
                continue
            
            found = False
            for a, b in itertools.permutations(nums, 2):
                if a % b == 0:
                    total_sum += a // b
                    found = True
                    break
            
        return total_sum
