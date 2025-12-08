class Day07Solver:
    def __init__(self, input_data: str):
        self.input_data = input_data.strip()
        self.grid = self._parse_input()

    def _parse_input(self):
        return [list(line) for line in self.input_data.split('\n')]

    def part1(self) -> "str | int":
        grid = self.grid
        height = len(grid)
        width = len(grid[0])
        
        # Find S
        active_beams = set()
        start_row = 0
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 'S':
                    active_beams.add(c)
                    start_row = r
                    break
            if active_beams:
                break
                
        split_count = 0
        
        # Simulate row by row
        # The beam moves downwards. In the example, S is at row 0.
        # The beam at S moves to row 1, then row 2...
        # We process what happens when the beam *enters* a cell.
        
        # Start from the row AFTER S, because S itself just emits the beam.
        # Actually, let's track the row we are currently entering.
        
        current_beams = active_beams
        
        for r in range(start_row + 1, height):
            next_beams = set()
            
            for c in current_beams:
                # Beam is entering cell (r, c)
                cell = grid[r][c]
                
                if cell == '^':
                    split_count += 1
                    # Split left and right
                    if c - 1 >= 0:
                        next_beams.add(c - 1)
                    if c + 1 < width:
                        next_beams.add(c + 1)
                else:
                    # Continue straight
                    next_beams.add(c)
            
            current_beams = next_beams
            if not current_beams:
                break
                
        return split_count

    def part2(self) -> "str | int":
        from collections import defaultdict
        
        grid = self.grid
        height = len(grid)
        width = len(grid[0])
        
        # Find S
        # beams[col_index] = number of timelines at that column
        current_beams = defaultdict(int)
        
        start_row = 0
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 'S':
                    current_beams[c] = 1
                    start_row = r
                    break
            if current_beams:
                break
                
        # Simulate row by row
        for r in range(start_row + 1, height):
            next_beams = defaultdict(int)
            
            for c, count in current_beams.items():
                # Beam is entering cell (r, c) with 'count' timelines
                cell = grid[r][c]
                
                if cell == '^':
                    # Split left and right
                    # Each timeline splits, so count is preserved for both paths
                    if c - 1 >= 0:
                        next_beams[c - 1] += count
                    if c + 1 < width:
                        next_beams[c + 1] += count
                else:
                    # Continue straight
                    next_beams[c] += count
            
            current_beams = next_beams
            if not current_beams:
                break
                
        return sum(current_beams.values())
