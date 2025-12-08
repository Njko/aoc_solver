from solvers.solver import Solver

class Day05Solver(Solver):
    def part1(self) -> "str | int":
        parts = self.input_data.strip().split('\n\n')
        range_lines = parts[0].split('\n')
        id_lines = parts[1].split('\n')
        
        ranges = []
        for line in range_lines:
            if not line.strip():
                continue
            start, end = map(int, line.strip().split('-'))
            ranges.append((start, end))
            
        fresh_count = 0
        for line in id_lines:
            if not line.strip():
                continue
            ingredient_id = int(line.strip())
            is_fresh = False
            for start, end in ranges:
                if start <= ingredient_id <= end:
                    is_fresh = True
                    break
            if is_fresh:
                fresh_count += 1
                
        return fresh_count

    def part2(self) -> "str | int":
        parts = self.input_data.strip().split('\n\n')
        range_lines = parts[0].split('\n')
        
        ranges = []
        for line in range_lines:
            if not line.strip():
                continue
            start, end = map(int, line.strip().split('-'))
            ranges.append((start, end))
            
        if not ranges:
            return 0
            
        # Sort ranges by start time
        ranges.sort(key=lambda x: x[0])
        
        merged_ranges = []
        current_start, current_end = ranges[0]
        
        for i in range(1, len(ranges)):
            next_start, next_end = ranges[i]
            
            # Check for overlap or adjacency (e.g., 3-5 and 6-8 should merge to 3-8)
            # The problem says ranges are inclusive.
            if next_start <= current_end + 1:
                current_end = max(current_end, next_end)
            else:
                merged_ranges.append((current_start, current_end))
                current_start, current_end = next_start, next_end
                
        merged_ranges.append((current_start, current_end))
        
        total_fresh = 0
        for start, end in merged_ranges:
            total_fresh += (end - start + 1)
            
        return total_fresh
