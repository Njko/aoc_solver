from collections import Counter
from collections import Counter
from aoc_agent.solver import Solver

class DaySolver(Solver):
    """
    Solves Day 5: Hydrothermal Venture
    
    Approach:
    - Parse line segments defined by (x1, y1) -> (x2, y2).
    - Use a `Counter` to track the number of lines covering each point on the grid.
    - Iterate through each line segment and generate all integer points between start and end.
    - Part 1: Consider only horizontal (y1=y2) and vertical (x1=x2) lines.
    - Part 2: Include diagonal lines (where |dx| == |dy|).
    - Count how many points have a coverage count >= 2.
    """
    def parse(self):
        lines = []
        for line in self.lines:
            if not line.strip():
                continue
            start, end = line.split(" -> ")
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            lines.append(((x1, y1), (x2, y2)))
        return lines

    def get_points(self, x1, y1, x2, y2):
        points = []
        dx = x2 - x1
        dy = y2 - y1
        
        steps = max(abs(dx), abs(dy))
        if steps == 0:
            return [(x1, y1)]
            
        x_step = dx // steps
        y_step = dy // steps
        
        for i in range(steps + 1):
            points.append((x1 + i * x_step, y1 + i * y_step))
            
        return points

    def solve_grid(self, include_diagonals=False):
        lines = self.parse()
        grid = Counter()
        
        for (x1, y1), (x2, y2) in lines:
            is_diag = (x1 != x2) and (y1 != y2)
            if is_diag and not include_diagonals:
                continue
                
            for p in self.get_points(x1, y1, x2, y2):
                grid[p] += 1
                
        return sum(1 for count in grid.values() if count >= 2)

    def part1(self) -> "str | int":
        return self.solve_grid(include_diagonals=False)

    def part2(self) -> "str | int":
        return self.solve_grid(include_diagonals=True)
