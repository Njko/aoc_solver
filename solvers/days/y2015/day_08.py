from aoc_agent.solver import Solver
import re

class DaySolver(Solver):
    def part1(self) -> "str | int":
        total_code = 0
        total_memory = 0
        
        for line in self.lines:
            total_code += len(line)
            # eval() is dangerous but for AoC input it's usually fine.
            # Alternatively, we can parse it manually.
            # The problem says only \\, \", and \xHH are used.
            # Let's use eval() for simplicity as it handles python string literals perfectly.
            total_memory += len(eval(line))
            
        return total_code - total_memory

    def part2(self) -> "str | int":
        total_code = 0
        total_encoded = 0
        
        for line in self.lines:
            total_code += len(line)
            # Encode: surround with quotes, escape backslashes and quotes.
            encoded = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
            total_encoded += len(encoded)
            
        return total_encoded - total_code
