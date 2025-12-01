from aoc_agent.solver import Solver

class DaySolver(Solver):
    def part1(self) -> "str | int":
        current = 50
        count = 0
        
        for line in self.lines:
            line = line.strip()
            if not line:
                continue
                
            direction = line[0]
            amount = int(line[1:])
            
            if direction == 'L':
                current = (current - amount) % 100
            elif direction == 'R':
                current = (current + amount) % 100
                
            if current == 0:
                count += 1
                
        return count

    def part2(self) -> "str | int":
        current = 50
        count = 0
        
        for line in self.lines:
            line = line.strip()
            if not line:
                continue
                
            direction = line[0]
            amount = int(line[1:])
            
            # We can simulate step by step if amount is small, but let's be efficient.
            # We are at 'current'. We move 'amount' steps.
            # The dial has 100 positions (0-99).
            # We hit 0 every 100 steps.
            
            # First, determine the distance to the next 0.
            if direction == 'R':
                # Moving forward: 50 -> 51 -> ... -> 99 -> 0
                dist_to_zero = (100 - current) % 100
                if dist_to_zero == 0: dist_to_zero = 100 # If at 0, next 0 is 100 steps away
                
                if amount >= dist_to_zero:
                    count += 1
                    remaining = amount - dist_to_zero
                    count += remaining // 100
                    
                current = (current + amount) % 100
                
            elif direction == 'L':
                # Moving backward: 50 -> 49 -> ... -> 1 -> 0
                dist_to_zero = current
                if dist_to_zero == 0: dist_to_zero = 100
                
                if amount >= dist_to_zero:
                    count += 1
                    remaining = amount - dist_to_zero
                    count += remaining // 100
                    
                current = (current - amount) % 100
                
        return count
