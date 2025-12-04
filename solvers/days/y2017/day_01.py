from solvers.solver import Solver

class Day01Solver(Solver):
    def part1(self) -> "str | int":
        data = self.input_data.strip()
        if not data:
            return 0
            
        total = 0
        length = len(data)
        
        for i in range(length):
            current_digit = int(data[i])
            next_digit = int(data[(i + 1) % length])
            
            if current_digit == next_digit:
                total += current_digit
                
        return total

    def part2(self) -> "str | int":
        data = self.input_data.strip()
        if not data:
            return 0
            
        total = 0
        length = len(data)
        step = length // 2
        
        for i in range(length):
            current_digit = int(data[i])
            next_digit = int(data[(i + step) % length])
            
            if current_digit == next_digit:
                total += current_digit
                
        return total
