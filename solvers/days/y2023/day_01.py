import re
from aoc_agent.solver import Solver

class DaySolver(Solver):
    """
    Solves Day 1: Trebuchet?!
    
    Approach:
    - Part 1: Iterate through each line, extract all numeric digits. Combine the first and last digit to form a number. Sum these numbers.
    - Part 2: Same as Part 1, but also search for spelled-out digits ("one", "two", etc.). 
      - Use `find()` to locate the first occurrence of any digit (numeric or spelled).
      - Use `rfind()` to locate the last occurrence.
      - Map spelled digits to their numeric values and compute the sum.
    """
    def part1(self) -> "str | int":
        total = 0
        for line in self.lines:
            digits = [c for c in line if c.isdigit()]
            if digits:
                val = int(digits[0] + digits[-1])
                total += val
        return total

    def part2(self) -> "str | int":
        total = 0
        digit_map = {
            "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
            "six": "6", "seven": "7", "eight": "8", "nine": "9"
        }
        # Add numeric digits to map for easy lookup
        for i in range(1, 10):
            digit_map[str(i)] = str(i)
            
        patterns = list(digit_map.keys())
        
        for line in self.lines:
            if not line:
                continue
                
            # Find first digit
            first_digit = None
            first_idx = len(line)
            
            for p in patterns:
                idx = line.find(p)
                if idx != -1 and idx < first_idx:
                    first_idx = idx
                    first_digit = digit_map[p]
            
            # Find last digit
            last_digit = None
            last_idx = -1
            
            for p in patterns:
                idx = line.rfind(p)
                if idx != -1 and idx > last_idx:
                    last_idx = idx
                    last_digit = digit_map[p]
            
            if first_digit and last_digit:
                val = int(first_digit + last_digit)
                total += val
                
        return total
