from solvers.solver import Solver


class Day20Solver(Solver):
    def __init__(self, input_data: str):
        super().__init__(input_data)
        self.input = self.input_data

    def _get_merged_ranges(self):
        ranges = []
        for line in self.input.strip().split('\n'):
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
        
        ranges.sort()
        
        merged = []
        if not ranges:
            return []
            
        current_start, current_end = ranges[0]
        
        for next_start, next_end in ranges[1:]:
            if next_start <= current_end + 1:
                current_end = max(current_end, next_end)
            else:
                merged.append((current_start, current_end))
                current_start, current_end = next_start, next_end
        
        merged.append((current_start, current_end))
        return merged

    def part1(self):
        merged_ranges = self._get_merged_ranges()
        
        if not merged_ranges or merged_ranges[0][0] > 0:
            return 0
            
        return merged_ranges[0][1] + 1

    def part2(self):
        merged_ranges = self._get_merged_ranges()
        max_ip = 4294967295
        allowed_count = 0
        last_end = -1
        
        for start, end in merged_ranges:
            allowed_count += start - (last_end + 1)
            last_end = end
            
        allowed_count += max_ip - last_end
        
        return allowed_count

