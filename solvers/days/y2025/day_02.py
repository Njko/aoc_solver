from solvers.solver import Solver

class Day02Solver(Solver):
    def _is_invalid(self, n: int) -> bool:
        s = str(n)
        if len(s) % 2 != 0:
            return False
        mid = len(s) // 2
        return s[:mid] == s[mid:]

    def part1(self) -> "str | int":
        total_invalid = 0
        
        # Input format: "start-end,start-end,..."
        # The input file might contain newlines, but the problem says "single long line".
        # We should handle potential newlines just in case or strip.
        content = self.input_data.strip()
        parts = content.split(',')
        
        for part in parts:
            if not part: continue
            start_str, end_str = part.split('-')
            start, end = int(start_str), int(end_str)
            
            for num in range(start, end + 1):
                if self._is_invalid(num):
                    total_invalid += num
                    
        return total_invalid

    def _is_invalid_part2(self, n: int) -> bool:
        s = str(n)
        length = len(s)
        # Try all possible substring lengths from 1 to length // 2
        for sub_len in range(1, length // 2 + 1):
            if length % sub_len == 0:
                sub = s[:sub_len]
                repeats = length // sub_len
                if sub * repeats == s:
                    return True
        return False

    def part2(self) -> "str | int":
        total_invalid = 0
        content = self.input_data.strip()
        parts = content.split(',')
        
        for part in parts:
            if not part: continue
            start_str, end_str = part.split('-')
            start, end = int(start_str), int(end_str)
            
            for num in range(start, end + 1):
                if self._is_invalid_part2(num):
                    total_invalid += num
                    
        return total_invalid
