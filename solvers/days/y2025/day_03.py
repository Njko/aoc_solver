from solvers.solver import Solver

class Day03Solver(Solver):
    def part1(self) -> "str | int":
        total_joltage = 0
        
        for line in self.lines:
            line = line.strip()
            if not line:
                continue
                
            # We need to find two digits at indices i and j (i < j)
            # such that int(line[i]) * 10 + int(line[j]) is maximized.
            
            # Optimization: The tens digit (d1) dominates.
            # We should look for the largest digit available at any position 
            # except the very last one (since it needs a digit after it).
            
            # 1. Find the largest digit d1 that appears at index < len(line) - 1
            max_d1 = -1
            # We can iterate backwards from 9 to 0 to find the largest d1 quickly
            for d in range(9, -1, -1):
                d_char = str(d)
                # Check if d_char appears in line before the last character
                # line.rfind(d_char) gives the last occurrence.
                # If the only occurrence is at the end, we need to check if there's another one.
                # But simpler: just iterate the string once or use list comprehension.
                
                # Let's just find all indices of d_char
                indices = [i for i, c in enumerate(line) if c == d_char]
                
                # We need at least one index < len(line) - 1
                valid_indices = [i for i in indices if i < len(line) - 1]
                
                if valid_indices:
                    max_d1 = d
                    break
            
            if max_d1 == -1:
                # Should not happen for valid input with length >= 2
                continue
                
            # 2. For the chosen max_d1, find the best d2
            # It's possible that max_d1 appears multiple times.
            # We need to check the max digit following ANY valid occurrence of max_d1.
            # Actually, if we have multiple max_d1s, the one that allows the largest d2 is best.
            # But d2 is just the max digit to the right.
            # So we want max(line[i+1:]) for all valid i where line[i] == max_d1.
            
            max_joltage_for_line = 0
            d_char = str(max_d1)
            for i, c in enumerate(line):
                if c == d_char and i < len(line) - 1:
                    # Find max digit after i
                    # We can optimize this too, but slicing is fine for typical line lengths
                    remaining = line[i+1:]
                    max_d2 = int(max(remaining))
                    joltage = max_d1 * 10 + max_d2
                    if joltage > max_joltage_for_line:
                        max_joltage_for_line = joltage
                        
            total_joltage += max_joltage_for_line
            
        return total_joltage

    def part2(self) -> "str | int":
        total_joltage = 0
        
        for line in self.lines:
            line = line.strip()
            if not line:
                continue
                
            # We need to find the largest subsequence of length 12.
            # This is a classic problem solvable with a greedy approach using a stack.
            # We want to keep the largest digits at the earliest possible positions.
            
            target_length = 12
            if len(line) < target_length:
                # Should not happen based on problem description
                continue
                
            to_discard = len(line) - target_length
            stack = []
            
            for digit_char in line:
                digit = int(digit_char)
                # While we can discard digits and the current digit is larger than the last one on stack
                while to_discard > 0 and stack and stack[-1] < digit:
                    stack.pop()
                    to_discard -= 1
                stack.append(digit)
                
            # If we still have digits to discard (e.g., decreasing sequence), discard from the end
            while to_discard > 0:
                stack.pop()
                to_discard -= 1
                
            # The stack should now have exactly target_length digits
            # (or we take the first target_length if something went wrong with logic, but it shouldn't)
            
            # Convert stack to number
            joltage_str = "".join(map(str, stack[:target_length]))
            total_joltage += int(joltage_str)
            
        return total_joltage
